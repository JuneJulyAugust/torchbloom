# Transformer Course Quality Iteration Log

## Purpose

This note records the 10 internal improvement passes used to raise the Transformer course MVP from a graph demo into a lesson, practice, lab, and project learning system. It is intended for future course authors, reviewers, and product work.

## Sources And Constraints

- Primary source: `raw/udl/textbook/pages/ch12-transformers/`
- Main edited course data: `web/src/lib/course/course-data.ts`
- Main edited course UI: `web/src/components/transformer-course-app.tsx`
- Main edited visual system: `web/src/app/globals.css`
- External design reference: OpenAI developers site style direction, interpreted as white background, restrained borders, high-contrast text, and content-first spacing.

The course content remains original TorchBloom synthesis grounded in UDL anchors. It should not copy long textbook captions or OCR prose.

## 10 Iterations

1. **Remove End-User Meta-Copy**
   - Finding: The lesson exposed pedagogy language instead of behaving like a product.
   - Change: Removed the explicit "Little-style move" sentence from the shared lesson template.
   - Evaluation: The app now speaks directly to the learner.

2. **Replace Slogan With Object Setup**
   - Finding: "Mix the value vectors" was true but not teachable without defining token, value, source index, and target index.
   - Change: Authored a concrete attention-output lesson beginning with tokens as sequence items.
   - Evaluation: A learner can now name the object being computed before seeing the formula.

3. **Add Shape Discipline**
   - Finding: Learners could confuse the attention row length with the output vector length.
   - Change: Added a value table and explicit shape check for `m`, `n`, value width, and output width.
   - Evaluation: The common error is caught by dimension reasoning.

4. **Add Worked Numeric Computation**
   - Finding: The selected node did not compute the equation it displayed.
   - Change: Added the full substitution `0.1[2,0] + 0.3[0,4] + 0.6[10,10] = [6.2,7.2]`.
   - Evaluation: The lesson now earns the title "Compute One Attention Output."

5. **Strengthen Practice**
   - Finding: Generated practice asked for recognition, not mastery.
   - Change: Replaced the selected node's practice with an authored vector computation and misconception feedback.
   - Evaluation: Passing practice requires computing the output, not selecting a mastery phrase.

6. **Deepen Prerequisite Nodes**
   - Finding: The selected node depends on values and softmax rows, but those nodes were still too compressed.
   - Change: Authored stronger lessons and practice for `attention.values`, `attention.softmax-row`, and `model.masked-self-attention`.
   - Evaluation: The route into the selected node is less abrupt.

7. **Fix Display Math Rendering**
   - Finding: Display equations were rendered as inline KaTeX because the delimiters were not block-separated.
   - Change: `EquationBlock` now passes newline-delimited display math to `MathMarkdown`.
   - Evaluation: Tests assert `.equationBox .katex-display` exists.

8. **Make The Lab Auditable**
   - Finding: The lab showed a mixed output but not the arithmetic that produced it.
   - Change: Added a weighted-sum ledger showing each share times each value vector and the final sum.
   - Evaluation: The lab now supports inspection and repair, not only reveal.

9. **Turn Project Into A Contract**
   - Finding: Project mode was pseudocode, not a guided build.
   - Change: Added a plain-Python project contract with helper functions, checkpoints, and masking/softmax checks.
   - Evaluation: The project has an artifact shape and success criteria.

10. **Retheme For Product Readability**
    - Finding: The previous cream/pastel surface and uneven mode controls read as prototype UI.
    - Change: Shifted to a white, neutral visual system with larger type, display-size equations, equal mode buttons, and restrained graph accents.
    - Evaluation: The lesson, practice, diagnostic, lab, and project modes now carry the main learning experience; the map remains available as support.

## Remaining Review Questions

- The long tail of 42 graph nodes still uses generated practice in places. The route-critical nodes now have authored practice, but the full course should eventually author every practice item.
- Source anchors are page-level. Future work should add equation and figure-level anchor metadata for review precision.
- The current project panel is a guided build contract, not an in-browser code runner. A later version can add a code workspace once the project contract stabilizes.
