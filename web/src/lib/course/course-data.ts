import type { Course } from './types'

export const course: Course = {
  id: 'udl-ch12-transformers',
  title: 'Transformer Mastery Course',
  subtitle: 'A Math Academy-style route through UDL Chapter 12 for an experienced learner.',
  target: 'Build and explain a tiny masked decoder from first principles.',
  nodes: [
    {
      id: 'math.weighted-average',
      title: 'Weighted Average',
      track: 'math',
      stage: 'foundations',
      summary:
        'Use weights that sum to one to mix values. Attention outputs are weighted mixtures, not single selected tokens.',
      sourceAnchors: ['raw/udl/textbook/pages/ch12-transformers/page_0208.md'],
      prerequisites: [],
      equation: 'y = w_1v_1 + w_2v_2 + ... + w_nv_n',
      littlePath: [
        'Start with three meaning cards and hand-made shares.',
        'Check that the shares add to one before mixing.',
        'Name the operation only after the learner has mixed values twice.',
      ],
      masteryEvidence: ['Compute a weighted mixture.', 'Explain why all shares must sum to one.'],
      practiceIds: ['practice.weighted-average'],
    },
    {
      id: 'math.dot-product',
      title: 'Dot Product As Match Score',
      track: 'math',
      stage: 'foundations',
      summary:
        'Multiply feature-by-feature and add. In attention, this becomes a score for how well a query matches a key.',
      sourceAnchors: ['raw/udl/textbook/pages/ch12-transformers/page_0210.md'],
      prerequisites: ['math.weighted-average'],
      equation: 'q dot k = q_1k_1 + q_2k_2 + ... + q_dk_d',
      littlePath: [
        'Compare two short feature lists before using notation.',
        'Ask which feature pair contributes the most to the final score.',
        'Contrast a high single feature with broad alignment across features.',
      ],
      masteryEvidence: ['Compute a dot product.', 'Interpret a larger dot product as stronger alignment.'],
      practiceIds: ['practice.dot-product'],
    },
    {
      id: 'prob.softmax-normalization',
      title: 'Softmax Normalization',
      track: 'probability',
      stage: 'foundations',
      summary:
        'Turn arbitrary scores into positive shares. Softmax makes the largest score influential without letting raw scores act as probabilities.',
      sourceAnchors: [
        'raw/udl/textbook/pages/ch12-transformers/page_0210.md',
        'raw/udl/textbook/pages/ch12-transformers/page_0239.md',
      ],
      prerequisites: ['math.weighted-average', 'math.dot-product'],
      equation: 'softmax(z_i) = exp(z_i) / sum_j exp(z_j)',
      littlePath: [
        'Show raw scores that cannot be shares because one is negative.',
        'Make every amount positive.',
        'Normalize the amounts so the row sums to one.',
        'Then reveal the compact softmax formula.',
      ],
      masteryEvidence: ['Identify why raw scores are not probabilities.', 'Predict the effect of a dominant score.'],
      practiceIds: ['practice.softmax-contrast'],
    },
    {
      id: 'code.list-indexing',
      title: 'Token Lists And Indexing',
      track: 'coding',
      stage: 'foundations',
      summary:
        'Represent a sentence as an ordered list of tokens and retrieve the token at a given position without losing sequence order.',
      sourceAnchors: ['raw/udl/textbook/pages/ch12-transformers/page_0207.md'],
      prerequisites: [],
      equation: 'tokens = ["the", "animal", "slept"]',
      littlePath: [
        'Make the sequence visible as positions.',
        'Ask what tokens[1] returns before using nested vectors.',
        'Use indexing mistakes as a reason positional information matters.',
      ],
      masteryEvidence: ['Read a token from a list.', 'Explain why order is not the same as set membership.'],
      practiceIds: [],
    },
    {
      id: 'transformer.qkv',
      title: 'Values, Queries, And Keys',
      track: 'transformers',
      stage: 'attention-core',
      summary:
        'Each token is projected into content to mix, a question to ask, and an address to match against.',
      sourceAnchors: [
        'raw/udl/textbook/pages/ch12-transformers/page_0209.md',
        'raw/udl/textbook/pages/ch12-transformers/page_0210.md',
      ],
      prerequisites: ['math.dot-product', 'code.list-indexing'],
      equation: 'V = X Omega_v, Q = X Omega_q, K = X Omega_k',
      littlePath: [
        'Give each token three roles: content, question, and address.',
        'Compute one query-key match by hand.',
        'Only then show the matrix notation.',
      ],
      masteryEvidence: ['Distinguish value from query and key.', 'Compute one query-key score.'],
      practiceIds: ['practice.qkv-roles'],
    },
    {
      id: 'transformer.self-attention',
      title: 'Self-Attention',
      track: 'transformers',
      stage: 'attention-core',
      summary:
        'Every token can route information from other tokens by matching its query against their keys and mixing their values.',
      sourceAnchors: [
        'raw/udl/textbook/pages/ch12-transformers/page_0208.md',
        'raw/udl/textbook/pages/ch12-transformers/page_0211.md',
      ],
      prerequisites: ['transformer.qkv', 'prob.softmax-normalization'],
      equation: 'A = softmax(QK^T / sqrt(d_k))V',
      littlePath: [
        'Start with a token asking which other token matters.',
        'Turn match scores into attention shares.',
        'Use the shares to mix values.',
        'Read one row of the attention table in plain language.',
      ],
      masteryEvidence: ['Compute one row of attention.', 'Explain attention as routing rather than lookup.'],
      practiceIds: ['practice.self-attention-row'],
    },
    {
      id: 'transformer.multi-head',
      title: 'Multiple Attention Heads',
      track: 'transformers',
      stage: 'attention-core',
      summary:
        'Several routing systems run in parallel, letting the model track different relationships before recombining them.',
      sourceAnchors: ['raw/udl/textbook/pages/ch12-transformers/page_0214.md'],
      prerequisites: ['transformer.self-attention'],
      equation: 'MhSa[X] = concat[H_1, ..., H_h] Omega_c',
      littlePath: [
        'Let one head track pronoun reference and another track local context.',
        'Show that heads are parallel, not repeated copies.',
        'Concatenate and project only after the roles are clear.',
      ],
      masteryEvidence: ['Explain why heads can specialize.', 'Reason about per-head dimensions.'],
      practiceIds: ['practice.multi-head'],
    },
    {
      id: 'transformer.layer',
      title: 'Transformer Layer',
      track: 'transformers',
      stage: 'transformer-block',
      summary:
        'A transformer layer updates each token representation with attention, residual addition, normalization, and a token-wise MLP.',
      sourceAnchors: [
        'raw/udl/textbook/pages/ch12-transformers/page_0215.md',
        'raw/udl/textbook/pages/ch12-transformers/page_0216.md',
      ],
      prerequisites: ['transformer.multi-head'],
      equation: 'X <- LayerNorm(X + MhSa(X))',
      littlePath: [
        'Preserve the old representation before updating it.',
        'Normalize after the update.',
        'Apply a small MLP to each token position.',
      ],
      masteryEvidence: ['Explain shape preservation.', 'Identify where the token-wise MLP is reused.'],
      practiceIds: ['practice.layer-shape'],
    },
    {
      id: 'transformer.masked-attention',
      title: 'Masked Attention',
      track: 'transformers',
      stage: 'decoder-project',
      summary:
        'A decoder must not look at future tokens. The mask forces future positions to receive zero attention share.',
      sourceAnchors: ['raw/udl/textbook/pages/ch12-transformers/page_0223.md'],
      prerequisites: ['transformer.self-attention'],
      equation: 'future score -> -infinity before softmax',
      littlePath: [
        'Play a next-token game where seeing the answer ruins the task.',
        'Mark future scores as forbidden.',
        'Show that softmax gives forbidden positions zero share.',
      ],
      masteryEvidence: ['Apply a future-token mask.', 'Explain why masking is needed for generation.'],
      practiceIds: ['practice.masking'],
    },
    {
      id: 'project.tiny-attention-router',
      title: 'Tiny Attention Router',
      track: 'project',
      stage: 'decoder-project',
      summary:
        'Build a small from-scratch attention route, inspect the attention table, then add a mask for next-token prediction.',
      sourceAnchors: [
        'raw/udl/textbook/pages/ch12-transformers/page_0222.md',
        'raw/udl/textbook/pages/ch12-transformers/page_0223.md',
      ],
      prerequisites: ['transformer.masked-attention', 'transformer.layer'],
      equation: 'next token ~ p(x_t | x_1, ..., x_{t-1})',
      littlePath: [
        'Tokenize a tiny sentence.',
        'Compute Q, K, and V with small fixed matrices.',
        'Inspect the attention row before generating a token.',
      ],
      masteryEvidence: ['Run the attention calculation.', 'Explain one generated next-token choice.'],
      practiceIds: [],
    },
    {
      id: 'extension.bert-gpt-vit',
      title: 'BERT, GPT, And Vision Extensions',
      track: 'transformers',
      stage: 'extensions',
      summary:
        'After the core route, compare encoder pretraining, decoder generation, cross-attention, long sequences, and vision transformers.',
      sourceAnchors: [
        'raw/udl/textbook/pages/ch12-transformers/page_0220.md',
        'raw/udl/textbook/pages/ch12-transformers/page_0227.md',
        'raw/udl/textbook/pages/ch12-transformers/page_0228.md',
      ],
      prerequisites: ['project.tiny-attention-router'],
      equation: 'extension route',
      littlePath: [
        'Classify each variant by what information it can see.',
        'Compare which attention matrix entries are allowed.',
        'Connect architecture choice to task type.',
      ],
      masteryEvidence: ['Compare encoder and decoder visibility.', 'Explain why images use patches.'],
      practiceIds: [],
    },
  ],
  diagnosticQuestions: [
    {
      id: 'weightedAverage',
      prompt: 'If values 1 and 3 get weights 0.2 and 0.8, what is the weighted average?',
      correctAnswer: '0.8',
      repairNodeId: 'math.weighted-average',
      options: [
        { value: '0.4', label: 'Weighted average: 0.4' },
        { value: '0.8', label: 'Weighted average: 2.6' },
      ],
    },
    {
      id: 'dotProduct',
      prompt: 'For q = [1, 2, 3] and k = [3, 1, 2], what is q dot k?',
      correctAnswer: '11',
      repairNodeId: 'math.dot-product',
      options: [
        { value: '11', label: 'Dot product: 11' },
        { value: '14', label: 'Dot product: 14' },
      ],
    },
    {
      id: 'softmax',
      prompt: 'What does softmax do to attention scores?',
      correctAnswer: 'largest-score-gets-largest-share',
      repairNodeId: 'prob.softmax-normalization',
      options: [
        { value: 'largest-score-gets-largest-share', label: 'Softmax assigns the largest score the largest share.' },
        { value: 'divide-raw-scores', label: 'Softmax divides raw scores by their sum.' },
      ],
    },
    {
      id: 'pythonIndexing',
      prompt: 'For tokens = ["we", "learn", "attention"], what does tokens[1] return?',
      correctAnswer: 'second-token',
      repairNodeId: 'code.list-indexing',
      options: [
        { value: 'first-token', label: 'tokens[1] returns "we".' },
        { value: 'second-token', label: 'tokens[1] returns "learn".' },
      ],
    },
    {
      id: 'masking',
      prompt: 'In a decoder, what should happen to future tokens?',
      correctAnswer: 'future-tokens-zero-share',
      repairNodeId: 'transformer.masked-attention',
      options: [
        { value: 'future-tokens-zero-share', label: 'Future tokens get zero attention share.' },
        { value: 'delete-all-old-tokens', label: 'Delete all old tokens and keep the future token.' },
      ],
    },
  ],
  practiceItems: [
    {
      id: 'practice.weighted-average',
      nodeId: 'math.weighted-average',
      kind: 'compute',
      prompt: 'Why does attention need weights that sum to one?',
      choices: [
        {
          id: 'shares',
          text: 'Because the output is a controlled mixture of value vectors.',
          correct: true,
          feedback: 'Right. A row of attention weights tells how much of each value vector is mixed.',
        },
        {
          id: 'largest-only',
          text: 'Because attention always selects only the largest value.',
          correct: false,
          feedback: 'Attention can put most weight on one value, but the output is still a mixture.',
        },
      ],
    },
    {
      id: 'practice.dot-product',
      nodeId: 'math.dot-product',
      kind: 'compute',
      prompt: 'What does a larger query-key dot product usually mean?',
      choices: [
        {
          id: 'alignment',
          text: 'The query and key are more aligned under the learned features.',
          correct: true,
          feedback: 'Yes. The score is a learned match signal.',
        },
        {
          id: 'longer-token',
          text: 'The source token is later in the sentence.',
          correct: false,
          feedback: 'Position can matter, but the dot product is comparing feature lists.',
        },
      ],
    },
    {
      id: 'practice.softmax-contrast',
      nodeId: 'prob.softmax-normalization',
      kind: 'explain',
      prompt: 'Why not use raw attention scores directly as probabilities?',
      choices: [
        {
          id: 'positive-exp',
          text: 'raw scores can be negative, so normalize positive exponentials',
          correct: true,
          feedback: 'Correct. Softmax makes positive amounts and normalizes them into shares.',
        },
        {
          id: 'divide',
          text: 'divide raw scores by their sum',
          correct: false,
          feedback: 'That fails with negative scores and does not give softmax behavior.',
        },
      ],
    },
    {
      id: 'practice.qkv-roles',
      nodeId: 'transformer.qkv',
      kind: 'explain',
      prompt: 'Which role carries the content that will be mixed?',
      choices: [
        { id: 'value', text: 'Value', correct: true, feedback: 'Yes. Values are the content to mix.' },
        { id: 'query', text: 'Query', correct: false, feedback: 'A query asks what this position is looking for.' },
      ],
    },
    {
      id: 'practice.self-attention-row',
      nodeId: 'transformer.self-attention',
      kind: 'shape',
      prompt: 'What does one row of an attention matrix describe?',
      choices: [
        {
          id: 'routing',
          text: 'How one query token distributes attention over source tokens.',
          correct: true,
          feedback: 'Right. Read each row as one token routing information from the sequence.',
        },
        {
          id: 'parameters',
          text: 'The learned value projection parameters.',
          correct: false,
          feedback: 'The attention matrix is computed per input; the projection matrices are learned parameters.',
        },
      ],
    },
    {
      id: 'practice.multi-head',
      nodeId: 'transformer.multi-head',
      kind: 'transfer',
      prompt: 'Why use multiple heads?',
      choices: [
        {
          id: 'parallel-relations',
          text: 'Different heads can track different relationships in parallel.',
          correct: true,
          feedback: 'Yes. Heads create several routing views before recombination.',
        },
        {
          id: 'same-repeat',
          text: 'They repeat the same attention calculation to average out noise.',
          correct: false,
          feedback: 'Heads are separately parameterized, not just repeated identical calculations.',
        },
      ],
    },
    {
      id: 'practice.layer-shape',
      nodeId: 'transformer.layer',
      kind: 'shape',
      prompt: 'Why does the transformer layer keep token count and feature width stable?',
      choices: [
        {
          id: 'stackable',
          text: 'So layers can be stacked and residual updates can be added back to the same shape.',
          correct: true,
          feedback: 'Correct. Shape preservation is what makes repeated layers possible.',
        },
        {
          id: 'remove-tokens',
          text: 'So every layer removes one token until only the answer remains.',
          correct: false,
          feedback: 'Transformer layers update all token representations; they do not remove one token per layer.',
        },
      ],
    },
    {
      id: 'practice.masking',
      nodeId: 'transformer.masked-attention',
      kind: 'debug',
      prompt: 'A decoder sees the word it is supposed to predict. What is wrong?',
      choices: [
        {
          id: 'mask-future',
          text: 'The future-token mask is missing or applied after softmax.',
          correct: true,
          feedback: 'Right. The mask must block future scores before softmax.',
        },
        {
          id: 'bigger-vocab',
          text: 'The vocabulary needs more tokens.',
          correct: false,
          feedback: 'Vocabulary size does not fix leakage from future positions.',
        },
      ],
    },
  ],
}
