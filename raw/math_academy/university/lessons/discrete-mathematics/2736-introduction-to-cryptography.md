# Introduction to Cryptography

Source: https://www.mathacademy.com/topics/2736?courseId=109
Topic ID: 2736

## Prerequisites

- [Modular Residues](../methods-of-proof/2786-modular-residues.md)

## Lesson

### Introduction

A **cipher** is a procedure for transforming or **encrypting** a message to conceal its meaning. The original message is said to be written in **plain text**, while the encrypted message is said to be written in **ciphertext**.

Ciphers often work by

1. translating each letter into a number called an **index**,

2. performing an operation on the index, and then

3. translating the number back into a letter.

The letters in the English alphabet are indexed as follows:

One of the simplest ciphers, the **Caesar cipher**, involves replacing each letter in a message with a different one $k$ places down the alphabet. If the alphabet consists of $n$ letters, then the plain text index $i_\text{plain}$ is translated into the ciphertext index $i_\text{cipher}$ as follows:

$$



i_\text{plain} + k \equiv i_\text{cipher} \: (\text{mod}\,n)



$$

For example, to encrypt the message $\text{HEY}$ using the Caesar cipher with the **key** $k=3$ over the English alphabet with $n=26$ letters, we do the following:

- Find the index of each letter of the word in the alphabet: H E Y $\color{blue}7$ $\color{blue}4$ $\color{blue}24$

- Add $k=3$ to each index modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indices: $\color{red}10$ $\color{red}7$ $\color{red}1$ K H B

Therefore, the encrypted message is $\text{KHB}.$

### Example: Encrypting a Message Using the Caesar Cipher

#### Question

Suppose we encrypt the five-letter English word $\text{ALBUM}$ to ciphertext using the Caesar cipher with key $k=16.$ Assuming that we use the usual English alphabet (shown below) during the encryption, what ciphertext word results from the encryption?

#### Explanation

To encrypt a word using the Caesar cipher with key $k=16$ over the English alphabet with $n=26$ letters, we do the following:

- Find the index of each letter of the word in the alphabet: A L B U M $\color{blue}0$ $\color{blue}11$ $\color{blue}1$ $\color{blue}20$ $\color{blue}12$

- Add $k=16$ to each index modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indices: $\color{red}16$ $\color{red}1$ $\color{red}17$ $\color{red}10$ $\color{red}2$ Q B R K C

Therefore, the answer is $\text{QBRKC}.$

### Decrypting a Message Using the Caesar Cipher

Earlier, we encrypted a message using the Caesar cipher with key $k=3$ over the English alphabet with $n=26$ letters. The resulting encrypted message was $\text{KHB}.$

However, suppose we send this message to a friend. How can they **decipher** or **decrypt** this message to reveal the original message?

Decrypting is the opposite of encrypting. Remember that to encrypt a message, we add the key to the indices of the letters. So, to *decrypt* a message, all we have to do is *subtract* the key:

$$



i_\text{cipher} - k \equiv i_\text{plain} \: (\text{mod}\,n)



$$

Let's recall the indices of the English alphabet and then decipher the message.

To decipher a message encrypted using the Caesar cipher with key $k=3$ over the English alphabet with $n=26$ letters, we do the following:

- Find the index of each letter of the ciphertext in the alphabet: K H B $\color{red}10$ $\color{red}7$ $\color{red}1$

- Subtract $k=3$ from each index modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indices: $\color{blue}7$ $\color{blue}4$ $\color{blue}24$ H E Y

We successfully recovered the original message, which was $\text{HEY}.$

### Example: Decrypting a Message Using the Caesar Cipher

#### Question

Suppose we encrypt a $4$-letter English word using the Caesar cipher with key $k=14$ and get the ciphertext $\text{QCBS}$ as a result. Assuming that during the encryption we used the usual English alphabet (shown below), what was the original (plain text) word?

#### Explanation

To decipher a message encrypted using the Caesar cipher with key $k=14$ over the English alphabet with $n=26$ letters, we do the following:

- Find the index of each letter of the ciphertext in the alphabet: Q C B S $\color{red}16$ $\color{red}2$ $\color{red}1$ $\color{red}18$

- Subtract $k=14$ from each index modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indices: $\color{blue}2$ $\color{blue}14$ $\color{blue}13$ $\color{blue}4$ C O N E

Therefore, the answer is $\text{CONE}.$
