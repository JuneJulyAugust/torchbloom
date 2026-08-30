# The Linear Cipher

Source: https://www.mathacademy.com/topics/2745?courseId=109
Topic ID: 2745

## Prerequisites

- [Introduction to Cryptography](./2736-introduction-to-cryptography.md)
- [Solving Linear Congruences](../methods-of-proof/4839-solving-linear-congruences.md)

## Lesson

### Introduction

The **linear cipher** is similar to the Caesar cipher. However, instead of adding the key, we multiply by the key. If the alphabet consists of $n$ letters, and the key is $a,$ then the plain text index $i_\textrm{plain}$ is translated into the ciphertext index $i_\textrm{cipher}$ as follows:

$$



a \cdot i_\textrm{plain} \equiv i_\textrm{cipher} \: (\text{mod}\,n)



$$

For example, let's encrypt the message $\textrm{HEY}$ using the linear cipher with key $a=3$ over the English alphabet with $n=26$ letters. First, we recall the indices of letters in the English alphabet:

Next, we do the following:

- Find the index of each letter of the word in the alphabet: H E Y $\color{blue}7$ $\color{blue}4$ $\color{blue}24$

- Multiply each index by $a=3$ modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indexes: $\color{red}21$ $\color{red}12$ $\color{red}20$ V M U

Therefore, the encrypted message is $\text{VMU}.$

### Example: Encrypting a Message Using the Linear Cipher

#### Question

Suppose we encrypt the four-letter English word $\text{TALK}$ to ciphertext using the linear cipher with key $a=7.$ Assuming that we use the usual English alphabet (shown below) during the encryption, what ciphertext word results from the encryption?

#### Explanation

To encrypt a word using the linear cipher with key $a=7$ over the English alphabet with $n=26$ letters, we do the following:

- Find the index of each letter of the word in the alphabet: T A L K $\color{blue}19$ $\color{blue}0$ $\color{blue}11$ $\color{blue}10$

- Multiply each index by $a=7$ modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indices: $\color{red}3$ $\color{red}0$ $\color{red}25$ $\color{red}18$ D A Z S

Therefore, the answer is $\text{DAZS}.$

### Decrypting a Message Using the Linear Cipher

Earlier, we encrypted a message using the linear cipher with key $a=3$ over the English alphabet with $n=26$ letters. The resulting encrypted message was $\textrm{VMU}.$

To decrypt this message, all we have to do is multiply by the inverse of the key:

$$



a^{-1} \cdot i_\textrm{cipher} \equiv i_\textrm{plain} \: (\text{mod}\,n)



$$

Let's recall the indices of the English alphabet and then decipher the message.

To decipher a message encrypted using the linear cipher with key $a=3$ over the English alphabet with $n=26$ letters, we do the following:

- Find the index of each letter of the ciphertext in the alphabet: V M U $\color{red}21$ $\color{red}12$ $\color{red}20$

- Find the inverse of $a=3$ modulo $26.$ To do that, we will use the extended Euclidean algorithm. First, we apply the forward reduction: Solving for the rightmost terms in the equations above, we get Then, we back-substitute: We can write this result in modulo $26,$ as follows: So we have $3 \cdot 9 \equiv 1 \: (\textrm{mod}\:26),$ which means that the inverse of $a=3$ modulo $26$ is $a^{-1}=9.$

- Multiply each index by $a^{-1}=9$ modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indices: $\color{blue}7$ $\color{blue}4$ $\color{blue}24$ H E Y

We successfully recovered the original message, which was $\text{HEY}.$

### Example: Decrypting a Message Using the Linear Cipher

#### Question

Suppose we encrypt a $4$-letter English word using the linear cipher with key $a=15$ and get the ciphertext $\text{ZAJU}$ as a result. Assuming that during the encryption we used the usual English alphabet (shown below), what was the original (plain text) word?

#### Explanation

To decipher a message encrypted using the linear cipher with key $a=15$ over the English alphabet with $n=26$ letters, we do the following:

- Find the index of each letter of the ciphertext in the alphabet: Z A J U $\color{red}25$ $\color{red}0$ $\color{red}9$ $\color{red}20$

- Find the inverse to $a=15$ modulo $26.$ To do that, we will use the extended Euclidean algorithm. First, we apply the forward reduction: Solving for the rightmost terms in the equations above, we get Then, we back-substitute: We can write this result in modulo $26,$ as follows: So we have $15 \cdot 7 \equiv 1 \: (\textrm{mod}\:26),$ which means that the inverse of $a=15$ modulo $26$ is $a^{-1}=7.$

- Multiply each index by $a^{-1}=7$ modulo $n=26\mathbin{:}$

- Find the letters that correspond to the new indices: $\color{blue}19$ $\color{blue}0$ $\color{blue}11$ $\color{blue}10$ T A L K

Therefore, the answer is $\text{TALK}.$
