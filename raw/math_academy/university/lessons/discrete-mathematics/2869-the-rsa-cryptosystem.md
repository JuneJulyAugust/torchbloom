# The RSA Cryptosystem

Source: https://www.mathacademy.com/topics/2869?courseId=109
Topic ID: 2869

## Prerequisites

- [Euler's Theorem](./2727-euler-s-theorem.md)
- [The Diffie-Hellman Protocol](./2877-the-diffie-hellman-protocol.md)
- [Multiplicative Inverses Modulo N](../methods-of-proof/4818-multiplicative-inverses-modulo-n.md)

## Lesson

### Introduction

The **RSA cryptographic algorithm** is a widely used public-key encryption algorithm that ensures secure communication between two parties over an unsecured network. It is based on the computational difficulty of factoring a product of large prime numbers.

Suppose we have two parties, Alice and Bob. Bob wishes to share a secret message with Alice over an unsecured network, keeping the message secret from Eve (our eavesdropper), who has access to all the information they share.

The RSA cryptographic algorithm allows Bob to share a secret message with Alice and can be described as follows:

- **Step 1:** Public key creation Alice selects two distinct prime numbers and computes the modulus and totient where is Euler's totient function. Thus, Alice has the following information: Two secret primes: and Modulus: Totient: Alice then chooses an encryption exponent such that Alice publishes the public key This is seen by both Bob and Eve.

- **Step 2:** Private key creation Alice computes the private decryption exponent such that Here, is simply the multiplicative inverse of modulo Alice's private key is

- **Step 3:** RSA Encryption Bob then encrypts a secret message (with) using the public key by computing The ciphertext is then sent to Alice.

- **Step 4:** RSA Decryption Finally, Alice recovers the original message using the private key by computing

We will formally justify this last step at the end of the lesson. Before that, let's get some practice at encrypting and decrypting messages using the RSA protocol.

### Encrypting Messages Using RSA

Suppose we encrypt the $3$-letter English word $\text{DOG}$ to ciphertext using the RSA cipher with the public key $(e,n)=(13,51).$ We'll assume that we use the usual English alphabet (shown above) during the encryption, where each letter is encrypted separately. Let's determine the ciphertext that results from the encryption.

*Hint: Use the mod function on your calculator or a software package to compute the required powers modulo $n.$*

To encrypt a word using the RSA cipher with the public key $(e,n)=(13,51)$ over the English alphabet, we do the following:

- Find the index of each letter of the word in the alphabet: D O G $\color{blue}3$ $\color{blue}14$ $\color{blue}6$

- Raise each index to the power of $e=13$ modulo $n=51\mathbin{:}$

Therefore, the ciphertext is

$$



12 \:\: 05 \:\: 27.



$$

### Example: Encrypting Messages Using the RSA Cipher

#### Question

Suppose we encrypt the $3$-letter English word $\text{BIT}$ to ciphertext using the RSA cipher with the public key $(e,n)=(19,65).$ Assuming that we use the usual English alphabet (shown below) during the encryption and each letter is encrypted separately, what ciphertext results from the encryption?

**

#### Explanation

To encrypt a word using the RSA cipher with the public key $(e,n)=(19,65)$ over the English alphabet, we do the following:

- Find the index of each letter of the word in the alphabet: B I T $\color{blue}1$ $\color{blue}8$ $\color{blue}19$

- Raise each index to the power of $e=19$ modulo $n=65\mathbin{:}$

Therefore, the ciphertext is

$$



01 \:\: 57 \:\: 59.



$$

### Decrypting Messages Using RSA

Suppose we encrypt a $3$-letter English word using the RSA cipher with the public key $(e,n)=(19,65)$ and get the ciphertext $41 \:\: 14 \:\: 59.$ Assuming we used the usual English alphabet (shown above) during the encryption and each letter was encrypted separately, how can we decrypt this and arrive at the original plain text word?

*Hint: Use the mod function on your calculator or a software package to compute the required powers modulo $n.$*

To decrypt a message using the RSA cipher, we need to know the private key.

Notice that $n=65 = 5 \times 13.$ Let's denote $p=5$ and $q=13.$ Then,

$$



\begin{aligned}𝜙(𝑛) & =(𝑝−1)(𝑞−1) \\ & =(5−1)(13−1) \\ & =4⋅12 \\ & =48.\end{aligned}



$$

For the RSA cipher with private key $(d,n),$ the first component $d$ is the multiplicative inverse of $e=19$ (the first component of the public key) modulo $\phi(n)=48{:}$

$$



d = e^{-1} \quad (\text{mod} \: 48)



$$

So, let's find the inverse of $e=19$ modulo $\phi(n)=48.$ To do that, we will use the extended Euclidean algorithm. First, we apply the forward reduction:

$$



\begin{aligned}\begin{matrix}48 & = & 19⋅2 & + & 10 \\ & ↙ & & ↙ & \\ 19 & = & 10⋅1 & + & 9 \\ & ↙ & & ↙ & \\ 10 & = & 9⋅1 & + & 1\end{matrix}\end{aligned}



$$

Solving for the rightmost terms in the equations above, we get

$$



\begin{aligned}10 & =48−19⋅2 \\ 9 & =19−10 \\ 1 & =10−9.\end{aligned}



$$

Then, we back-substitute:

$$



\begin{aligned}1 & =10−9 \\ & =10−(19−10) \\ & =10⋅2−19 \\ & =(48−19⋅2)⋅2−19 \\ & =48⋅2+19⋅(−5)\end{aligned}



$$

We can write this result in modulo $48,$ as follows:

$$



\begin{aligned}48⋅2+19⋅(−5) & ≡1 & & (mod\,48) \\ 19⋅43 & ≡1 & & (mod\,48)\end{aligned}



$$

So we have $19 \cdot 43 \equiv 1 \: (\text{mod}\:48),$ which means that the inverse of $e=19$ modulo $48$ is $e^{-1}=43.$

Thus, our private key is $(d,n) = (43,65).$

Now, to decrypt a word using the RSA cipher with the private key $(d,n)=(43,65)$ over the English alphabet, we do the following:

- Raise each index to the power of $d=43$ modulo $n=65\mathbin{:}$

- Find the letters that correspond to the new indexes: $\color{blue}11$ $\color{blue}14$ $\color{blue}19$ L O T

Therefore, the plaintext was

$$



L \:\: O \:\: T.



$$

### Example: Decrypting Messages Using the RSA Cipher When the Private Key is Given

#### Question

Suppose we encrypt a $3$-letter English word using the RSA cipher with the private key $(d,n)=(13,55)$ and get the ciphertext $52 \:\: 49 \:\: 53$ as a result. Assuming that during the encryption, we used the usual English alphabet (shown below) and each letter was encrypted separately, what was the original (plain text) word?

**

#### Explanation

To decrypt a word using the RSA cipher with the private key $(d,n)=(13,55)$ over the English alphabet, we do the following:

- Raise each index to the power of $d=13$ modulo $n=55\mathbin{:}$

- Find the letters that correspond to the new indexes: $\color{blue}17$ $\color{blue}4$ $\color{blue}3$ R E D

Therefore, the plaintext was

$$



R \:\: E \:\: D.



$$

### Example: Decrypting Messages Using the RSA Cipher When the Public Key is Given

#### Question

Suppose we encrypt a $3$-letter English word using the RSA cipher with the public key $(e,n)=(7,33)$ and get the ciphertext $15 \:\: 16 \:\: 13$ as a result. Assuming that during the encryption, we used the usual English alphabet (shown below) and each letter was encrypted separately, what was the original (plain text) word?

**

#### Explanation

To decrypt a message using the RSA cipher, we need to know its corresponding private key.

Notice that $n=33 = 3 \times 11.$ Let's denote $p=3$ and $q=11.$ Then,

$$



\begin{aligned}𝜙(𝑛) & =(𝑝−1)(𝑞−1) \\ & =(3−1)(11−1) \\ & =2⋅10 \\ & =20.\end{aligned}



$$

For the RSA cipher with the private key $(d,n),$ the first component $d$ is the multiplicative inverse of $e=7$ (the first component of the public key) modulo $\phi(n)=20{:}$

$$



d = e^{-1} \quad (\text{mod} \: 20)



$$

So, let's find the inverse of $e=7$ modulo $\phi(n)=20.$ To do that, we will use the extended Euclidean algorithm. First, we apply the forward reduction:

$$



\begin{aligned}\begin{matrix}20 & = & 7⋅2 & + & 6 \\ & ↙ & & ↙ & \\ 7 & = & 6⋅1 & + & 1\end{matrix}\end{aligned}



$$

Solving for the rightmost terms in the equations above, we get

$$



\begin{aligned}6 & =20−7⋅2 \\ 1 & =7−6.\end{aligned}



$$

Then, we back-substitute:

$$



\begin{aligned}1 & =7−6 \\ & =7−(20−7⋅2) \\ & =7⋅3−20 \\ & =7⋅3+20⋅(−1)\end{aligned}



$$

We can write this result in modulo $20,$ as follows:

$$



\begin{aligned}7⋅3+20⋅(−1) & ≡1 & & (mod\,20) \\ 7⋅3 & ≡1 & & (mod\,20)\end{aligned}



$$

So we have $7 \cdot 3 \equiv 1 \: (\text{mod}\:20),$ which means that the inverse of $e=7$ modulo $20$ is $e^{-1}=3.$

Thus, our private key is $(d,n) = (3,33).$

Now, to decrypt a word using the RSA cipher with the private key $(d,n)=(3,33)$ over the English alphabet, we do the following:

- Raise each index to the power of $d=3$ modulo $n=33\mathbin{:}$

- Find the letters that correspond to the new indexes: $\color{blue}09$ $\color{blue}04$ $\color{blue}19$ J E T

Therefore, the plaintext was

$$



J \:\: E \:\: T.



$$

### Explaining Why the Decryption Step Works

Recall that in the RSA cryptosystem, we have the public key $(e,n)$ and the private key $(d,n),$ where

- $p$ and $q$ are (large) primes,

- $n=pq$

- $\phi(n)=(p-1)(q-1),$ and

- $e \cdot d \equiv 1 \: (\text{mod} \: \phi(n)).$

The message $M$ (with $M < n$) is encrypted by computing

$$



C \equiv M^e \quad (\text{mod} \: n),



$$

whereas $C$ is decrypted by computing

$$



M \equiv C^d \quad (\text{mod} \: n).



$$

Let's now show that after computing $C^d$ modulo $n,$ we indeed restore the original message $M.$

We have

$$



\begin{aligned}𝐶^{𝑑} & ≡(𝑀^{𝑒})^{𝑑} & & \,(mod\,𝑛) \\ & ≡𝑀^{𝑒𝑑} & & \,(mod\,𝑛).\end{aligned}



$$

Now, notice that since $e \cdot d \equiv 1 \: (\text{mod} \: \phi(n)),$ we have

$$



ed = 1 + k \phi(n)



$$

for some integer $k.$ Thus,

$$



\begin{aligned}𝑀^{𝑒𝑑} & ≡𝑀^{1+𝑘𝜙(𝑛)} & & \,(mod\,𝑛) \\ & ≡𝑀⋅(𝑀^{𝜙(𝑛)})^{𝑘} & & \,(mod\,𝑛).\end{aligned}



$$

Next, we can assume that $\gcd(M,n)=1.$ Indeed, the probability that $M$ and $n$ will have a common divisor greater than $1$ is extremely small when the primes $p$ and $q$ are large. Moreover, if this happens, the private key will be compromised anyway. Therefore, according to Euler's theorem, $M^{\phi(n)} \equiv 1 \: (\text{mod} \: n).$

Finally, we have

$$



\begin{aligned}𝑀⋅(𝑀^{𝜙(𝑛)})^{𝑘} & ≡𝑀⋅1^{𝑘} & & \,(mod\,𝑛) \\ & ≡𝑀⋅1 & & \,(mod\,𝑛) \\ & ≡𝑀 & & \,(mod\,𝑛).\end{aligned}



$$

### Justifying the RSA Cryptosystem

Why is the RSA cryptosystem expected to be secure?

Suppose you are Eve, an attacker eavesdropping on two parties, Alice and Bob, who are using RSA to send secret messages to each other. This means you have access to

- the public key $(e, n)$, consisting of

- the public encryption exponent $e$ and

- the modulus $n$

but you do *not* have access to

- the factorization $n = pq$

- the totient $\phi(n) = (p-1)(q-1)$

- the private decryption exponent $d \equiv e^{-1} \pmod{\phi(n)}.$

Furthermore, whenever Alice or Bob encrypts a secret message $M$ by computing

$$



C \equiv M^e \pmod{n}



$$

you have access to the resulting ciphertext $C.$ RSA is secure if it is difficult to use what you have access to $(e, n$, and $C)$ to compute the original plaintext $M.$ This problem is known as the **RSA problem.**

In this lesson, you solved the RSA problem for small values of $n$, such as $n = 33$, by factoring $n = pq$ into a product of two primes. Given this factorization you computed $\phi(n) = (p - 1)(q - 1)$, which let you compute $d \equiv e^{-1} \pmod{\phi(n)}$, which finally let you compute $M \equiv C^d \pmod{n}.$

In general, factoring $n$ is the most efficient known method of solving the RSA problem, and no cleverer ways of solving the RSA problem without factoring $n$ are known.

Therefore, it is widely believed (but not proven!) that solving the RSA problem is as difficult as factoring $n.$ In practical implementations of RSA, $n$ is very large. For very large numbers, factoring is widely believed (but not proven!) to be a difficult problem with no known efficient solution in a certain precise technical sense.

### The Magnitude of N

How large is $n$ in practice? The National Institute of Standards and Technology (NIST) currently recommends a key size of $2048$ bits, meaning $n$ should have $2048$ binary digits. $2^{2047}$ is about $1.6 \times 10^{616}$, so numbers this large have $616$ decimal digits. This suggests the NIST believes numbers this large are currently still difficult to factor, and should remain so for some time.

To compare this to the current state-of-the-art for factoring, in 1991 RSA Laboratories ran a challenge, the **RSA Factoring Challenge**, challenging researchers to factor specific large numbers, the **RSA numbers**, which are all products $n = pq$ of two large primes, as used in RSA. The largest of the RSA numbers which has been factored so far is called **RSA-250**; it is an $829$-bit number (with $250$ decimal digits), namely

and it was factored in 2020 using $2700$ CPU core-years of computation into the following product of two primes:

The smallest RSA number which has not been factored so far is called **RSA-260**; it is an $895$-bit number (with $260$ decimal digits), namely

The hard drive of the computer that generated the RSA numbers was destroyed. This means that RSA-260 is known to factor into a product of two primes, but *nobody* knows what they are!
