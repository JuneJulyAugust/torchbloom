#!/usr/bin/env node

/**
 * Audit every Math Academy Markdown math span with KaTeX.
 *
 * Usage:
 *   node scripts/audit-math-academy-katex.cjs [path] [--summary] [--samples]
 *   node scripts/audit-math-academy-katex.cjs --fix
 *
 * `--fix` intentionally contains only inspected, semantics-preserving repairs.
 */

const fs = require("node:fs");
const path = require("node:path");
const katex = require(path.join(__dirname, "..", "web", "node_modules", "katex"));

const fixMode = process.argv.includes("--fix");
const summaryOnly = process.argv.includes("--summary");
const samplesOnly = process.argv.includes("--samples");
const targetArgument = process.argv.slice(2).find((argument) => !argument.startsWith("--"));
const target = path.resolve(targetArgument || path.join(__dirname, "..", "raw", "math_academy"));

function markdownFiles(root) {
  if (fs.statSync(root).isFile()) return root.endsWith(".md") ? [root] : [];
  const files = [];
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    const fullPath = path.join(root, entry.name);
    if (entry.isDirectory()) files.push(...markdownFiles(fullPath));
    else if (entry.isFile() && entry.name.endsWith(".md")) files.push(fullPath);
  }
  return files;
}

function escaped(text, index) {
  let count = 0;
  for (let cursor = index - 1; cursor >= 0 && text[cursor] === "\\"; cursor -= 1) count += 1;
  return count % 2 === 1;
}

function lineNumber(text, index) {
  let line = 1;
  for (let cursor = 0; cursor < index; cursor += 1) if (text[cursor] === "\n") line += 1;
  return line;
}

function extractMath(text) {
  const expressions = [];
  const failures = [];
  let cursor = 0;
  let fence = null;
  while (cursor < text.length) {
    const atLineStart = cursor === 0 || text[cursor - 1] === "\n";
    if (atLineStart) {
      const match = text.slice(cursor).match(/^( {0,3})(`{3,}|~{3,})/);
      if (match) {
        const marker = match[2][0];
        const length = match[2].length;
        if (!fence) fence = { marker, length };
        else if (fence.marker === marker && length >= fence.length) fence = null;
        cursor += match[0].length;
        continue;
      }
    }
    if (fence || text[cursor] !== "$" || escaped(text, cursor)) {
      cursor += 1;
      continue;
    }
    const display = text[cursor + 1] === "$";
    const openingLength = display ? 2 : 1;
    const start = cursor + openingLength;
    let end = start;
    if (display) {
      while (end < text.length - 1 && !(text[end] === "$" && text[end + 1] === "$" && !escaped(text, end))) end += 1;
      if (end >= text.length - 1) {
        failures.push({ line: lineNumber(text, cursor), kind: "delimiter", message: "Unclosed display math delimiter" });
        break;
      }
    } else {
      while (end < text.length && !(text[end] === "$" && !escaped(text, end))) {
        if (text[end] === "\n") break;
        end += 1;
      }
      if (end >= text.length || text[end] === "\n") {
        failures.push({ line: lineNumber(text, cursor), kind: "delimiter", message: "Unclosed inline math delimiter" });
        cursor = end + 1;
        continue;
      }
    }
    expressions.push({ expression: text.slice(start, end), display, line: lineNumber(text, cursor) });
    cursor = end + openingLength;
  }
  return { expressions, failures };
}

function normalizeMatrices(text) {
  let result = "";
  let cursor = 0;
  while (cursor < text.length) {
    const match = text.slice(cursor).match(/^\\matrix\s*\{/);
    if (!match) {
      result += text[cursor];
      cursor += 1;
      continue;
    }
    const bodyStart = cursor + match[0].length;
    let depth = 1;
    let end = bodyStart;
    while (end < text.length && depth) {
      if (text[end] === "{" && !escaped(text, end)) depth += 1;
      else if (text[end] === "}" && !escaped(text, end)) depth -= 1;
      end += 1;
    }
    if (depth) {
      result += text[cursor];
      cursor += 1;
      continue;
    }
    result += `\\begin{matrix}${text.slice(bodyStart, end - 1)}\\end{matrix}`;
    cursor = end;
  }
  return result;
}

function normalizeNestedAligned(text) {
  let depth = 0;
  return text.replace(/\\(begin|end)\{aligned\}/g, (match, command) => {
    if (command === "begin") {
      const replacement = depth > 0 ? "\\begin{matrix}" : match;
      depth += 1;
      return replacement;
    }
    depth = Math.max(0, depth - 1);
    return depth > 0 ? "\\end{matrix}" : match;
  });
}

function normalizeVerifiedMathAcademyText(text) {
  // The source sometimes places a Unicode radical immediately inside LaTeX's
  // `\\sqrt{...}`. It is a duplicate glyph, not a nested square root.
  let result = text.replace(/\\sqrt\{√/g, "\\sqrt{");
  // Source-side display limits use MathJax's invalid `operator_\\limits{}`
  // shape. The equivalent KaTeX form has `\\limits` before the subscript.
  result = result.replace(/\\(lim|int|iint)_\\limits\s*\{/g, "\\$1\\limits_{");
  // A line-break spacing option must follow KaTeX's two-backslash row break.
  result = result.replace(/\\{3}\[([^\]\n]*)\]/g, "\\\\[$1]");
  result = result.replace(/(^|[^\\])\\\[(-?\d+(?:\.\d+)?(?:pt|ex|em))\]/g, "$1\\\\[$2]");
  // KaTeX already supplies these functions; source declarations conflict.
  result = result.replace(/\\newcommand\{\\(?:arsinh|arcosh|artanh|arsech|arcsch|arcoth|coth|cosh|sinh|tanh|sech|csch)\}\{\\mathop\{\\rm [^}]+\}\\nolimits\}\s*/g, "");
  result = result.replace(/\\nolimits\}\s*/g, "");
  for (const name of ["arsinh", "arcosh", "artanh", "arsech", "arcsch", "arcoth", "sech", "csch"]) {
    result = result.replace(new RegExp(String.raw`\\${name}\b`, "g"), `\\operatorname{${name}}`);
    result = result.replace(new RegExp(String.raw`\\newcommand\{\\operatorname\{${name}\}\}`, "g"), `\\newcommand{\\${name}}`);
  }
  // Blank answer placeholders and unbraced subscripts are source text rather
  // than valid TeX operators.
  result = result.replace(/_{2,}/g, "\\underline{\\hspace{3em}}");
  result = result.replace(/_\\(min|max)\b/g, "_{\\$1}");
  result = result.replace(/_\\boldsymbol(\{[^{}]+\})/g, "_{\\boldsymbol$1}");
  result = result.replace(/\^\\sqrt\s*(\{[^{}]+\}|[A-Za-z0-9])/g, "^{\\sqrt $1}");
  result = result.replace(/(_\{[^{}]*\})\^\{\}/g, "$1");
  result = result.replace(/\\overset\{([^{}]+)\}\{\^\}/g, "\\hat{$1}");
  // These source formatting commands have direct KaTeX equivalents.
  result = result.replace(/\\enclose\{longdiv\}\{([^{}]*)\}/g, "\\overline{$1}");
  result = result.replace(/\\enclose\{longdiv\}\{/g, "\\overline{");
  result = result.replace(/\\raise\{[^{}]*\}\{([^{}]*)\}/g, "$1");
  result = result.replace(/\\color\{\}/g, "");
  result = result.replace(/\\color\{\\(green|red|blue)\}/g, "\\color{$1}");
  result = result.replace(/\\textrm\{([^{}]*)\}/g, "\\text{$1}");
  result = result.replace(/\\phantom\{\\text\{([^{}]*)\}\}/g, "\\phantom{\\mathrm{$1}}");
  // Repair malformed source wrappers around annotations and embedded matrices.
  result = result.replace(/\\overset\{\\overset\\begin\{aligned\}/g, "\\overset{\\begin{aligned}");
  result = result.replace(/\\overset\{\\overset\{/g, "\\overset{");
  result = result.replace(/\{\\underset\{\}\\begin\{aligned\}/g, "{\\begin{aligned}");
  result = result.replace(/\\overset\\begin\{aligned\}/g, "\\overset{\\begin{aligned}");
  result = result.replace(/\\frac\\begin\{aligned\}/g, "\\frac{\\begin{aligned}");
  // The exporter occasionally inserts an empty second argument before the
  // actual annotation: `\\overset{top}{}}{base}`.
  result = result.replace(/\\overset\{([^{}]*)\}\{\}\}\{/g, "\\overset{$1}{");
  result = result.replace(/\\underset\{([^{}]*)\}\{\}\}\{/g, "\\underset{$1}{");
  result = result.replace(/\\end\{aligned\}\}\{\}\}\{/g, "\\end{aligned}}{");
  result = result.replace(/\\end\{aligned\}\}\\begin\{aligned\}/g, "\\end{aligned}}{\\begin{aligned}");
  result = result.replace(/\\end\{aligned\}\}\}/g, "\\end{aligned}}");
  result = result.replace(/\\frac\{#/g, "\\frac{\\#");
  result = result.replace(/\\text\{#/g, "\\text{\\#");
  // Most exported matrices contain no nested braces; convert these to KaTeX's
  // environment syntax without touching inline text around them.
  result = normalizeMatrices(result);
  result = normalizeNestedAligned(result);
  result = result.replace(/2−𝑥\^\{2\}\^\{2\}/g, "(2−𝑥^{2})^{2}");
  return result;
}

const warning = console.warn;
const error = console.error;
console.warn = () => {};
console.error = () => {};

const failures = [];
let expressionCount = 0;
let changedFiles = 0;
const files = markdownFiles(target);
for (const filePath of files) {
  let text = fs.readFileSync(filePath, "utf8");
  if (fixMode) {
    const normalized = normalizeVerifiedMathAcademyText(text);
    if (normalized !== text) {
      fs.writeFileSync(filePath, normalized);
      text = normalized;
      changedFiles += 1;
    }
  }
  const extracted = extractMath(text);
  expressionCount += extracted.expressions.length;
  for (const failure of extracted.failures) failures.push({ filePath, ...failure });
  for (const entry of extracted.expressions) {
    try {
      katex.renderToString(entry.expression, { displayMode: entry.display, strict: false, throwOnError: true });
    } catch (caught) {
      failures.push({
        filePath,
        line: entry.line,
        kind: entry.display ? "display" : "inline",
        message: caught.message.replace(/\s+/g, " "),
        expression: entry.expression.replace(/\s+/g, " ").trim(),
      });
    }
  }
}

console.warn = warning;
console.error = error;
if (fixMode) console.log(`Applied verified repairs to ${changedFiles.toLocaleString()} Markdown files.`);
console.log(`KaTeX audit: ${expressionCount.toLocaleString()} expressions in ${files.length.toLocaleString()} Markdown files.`);
if (!failures.length) {
  console.log("KaTeX audit passed: no malformed delimiters or parse failures.");
  process.exit(0);
}
console.log(`KaTeX audit failed: ${failures.length.toLocaleString()} issue(s).`);
if (summaryOnly) {
  const groups = new Map();
  for (const failure of failures) {
    const key = `${failure.kind}: ${failure.message.replace(/ at position .*/, "")}`;
    groups.set(key, (groups.get(key) || 0) + 1);
  }
  for (const [key, count] of [...groups.entries()].sort((a, b) => b[1] - a[1])) console.log(`${count}  ${key}`);
  process.exit(1);
}
if (samplesOnly) {
  const samples = new Map();
  for (const failure of failures) {
    const key = `${failure.kind}: ${failure.message.replace(/ at position .*/, "")}`;
    if (!samples.has(key)) samples.set(key, failure);
  }
  for (const [, failure] of samples) {
    console.log(`${path.relative(process.cwd(), failure.filePath)}:${failure.line}: ${failure.kind}: ${failure.message}`);
    if (failure.expression) console.log(`  ${failure.expression.slice(0, 500)}`);
  }
  process.exit(1);
}
for (const failure of failures.slice(0, 200)) {
  console.log(`${path.relative(process.cwd(), failure.filePath)}:${failure.line}: ${failure.kind}: ${failure.message}`);
  if (failure.expression) console.log(`  ${failure.expression.slice(0, 300)}`);
}
process.exit(1);
