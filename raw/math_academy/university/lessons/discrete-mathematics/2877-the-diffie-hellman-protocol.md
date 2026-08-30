# The Diffie-Hellman Protocol

Source: https://www.mathacademy.com/topics/2877?courseId=109
Topic ID: 2877

## Prerequisites

- [The Multiplication Properties of Modular Arithmetic](../methods-of-proof/2674-the-multiplication-properties-of-modular-arithmetic.md)
- [Introduction to Cryptography](./2736-introduction-to-cryptography.md)

## Lesson

### Introduction

The **Diffie-Hellman** shared secret exchange protocol is a **public key cryptographic algorithm** that allows two parties to share a secret message over an insecure communication channel. It uses modular exponentiation to derive the shared secret without directly transmitting it.

The discovery of the Diffie-Hellman protocol laid the foundations for many modern cryptographic protocols for securely transferring online information. Before considering the Diffie-Hellman algorithm in detail, let's review its mathematical foundations.

Suppose that we need to compute $8^{24} \:\text{mod}\: 59.$ To do that efficiently, we proceed as follows:

First, we write $24$ as a sum of powers of $2{:}$

$$



24 = 2^4+2^3 = 16+8



$$

So, we have

$$



8^{24} = 8^{16+8} = 8^{16} \cdot 8^{8}.



$$

Now, we compute the exponents modulo $59$ using consecutive squaring:

$$



\begin{aligned}8^{2} & ≡64≡5 & \,(mod\,59) \\ 8^{4} & ≡5^{2}≡25 & \,(mod\,59) \\ 8^{8} & ≡25^{2}≡625≡35 & \,(mod\,59) \\ 8^{16} & ≡35^{2}≡1\,225≡45 & \,(mod\,59)\end{aligned}



$$

Finally, by multiplying the highlighted exponents, we get the following:

$$



\begin{aligned}8^{24} & ≡8^{16}⋅8^{8} & \,(mod\,59) & \\ & ≡45⋅35 & \,(mod\,59) & \\ & ≡1\,575 & \,(mod\,59) & \\ & ≡26⋅59+41 & \,(mod\,59) & \\ & ≡41 & \,(mod\,59) & .\end{aligned}



$$

### Example: Representing an Expression in a Suitable Form for Exponentiation

#### Question

Which of the following is equivalent to $11^{49} \: \text{mod}\: 73?$

1. $(16 \cdot 4 \cdot 11) \: \text{mod} \:73$

2. $(4 \cdot 2 \cdot 48) \: \text{mod} \: 73$

3. $(16 \cdot 2 \cdot 48) \: \text{mod} \: 73$

**

#### Explanation

First, we write $49$ as a sum of powers of $2{:}$

$$



49 =2^5 + 2^4 + 2^0 = 32+16+1



$$

So, we have

$$



11^{49} = 11^{32 + 16 + 1} = 11^{32} \cdot 11^{16} \cdot 11^{1}.



$$

Now, we can take the corresponding values from the given table:

Therefore, we obtain

$$



\begin{aligned}11^{49} & ≡11^{32}⋅11^{16}⋅11^{1} & \,(mod\,73) & \\ & ≡16⋅4⋅11 & \,(mod\,73) & .\end{aligned}



$$

Therefore, the correct answer is "I only."

### Example: Exponentiation by Squaring Given the Key Powers

#### Question

Use the above table containing some powers of $8$ modulo $67$ to compute $8^{28} \:\text{mod}\: 67.$

#### Explanation

First, we write $28$ as a sum of powers of $2{:}$

$$



28 = 2^4+2^3 +2^2 = 16 + 8 + 4



$$

So, we have

$$



8^{28} = 8^{16 +8 +4} = 8^{16} \cdot 8^{8} \cdot 8^4.



$$

Now, we can take the corresponding values from the given table:

Therefore, we obtain

$$



\begin{aligned}8^{28} & ≡8^{16}⋅8^{8}⋅8^{4} & \,(mod\,67) & \\ & ≡62⋅14⋅9 & \,(mod\,67) & \\ & ≡7812 & \,(mod\,67) & \\ & ≡116⋅67+40 & \,(mod\,67) & \\ & ≡40 & \,(mod\,67) & .\end{aligned}



$$

### Example: Exponentiation by Squaring

#### Question

Compute $9^{22} \:\text{mod}\: 37.$

#### Explanation

First, we write $22$ as a sum of powers of $2{:}$

$$



22 = 2^4+2^2+2^1 = 16 + 4 + 2



$$

So, we have

$$



9^{22} = 9^{16 + 4 + 2} =9^{16} \cdot 9^{4} \cdot 9^{2}.



$$

Now, we compute the exponents modulo $37$ using consecutive squaring:

$$



\begin{aligned}9^{2} & ≡81≡7 & \,(mod\,37) \\ 9^{4} & ≡7^{2}≡49≡12 & \,(mod\,37) \\ 9^{8} & ≡12^{2}≡144≡33 & \,(mod\,37) \\ 9^{16} & ≡33^{2}≡1\,089≡16 & \,(mod\,37) \\ 9^{32} & ≡16^{2}≡256≡34 & \,(mod\,37)\end{aligned}



$$

Finally, by multiplying the obtained exponents, we get

$$



\begin{aligned}9^{22} & ≡9^{16}⋅9^{4}⋅9^{2} & \,(mod\,37) & \\ & ≡16⋅12⋅7 & \,(mod\,37) & \\ & ≡1\,344 & \,(mod\,37) & \\ & ≡36⋅37+12 & \,(mod\,37) & \\ & ≡12 & \,(mod\,37) & .\end{aligned}



$$

### The Diffie-Hellman Protocol

Suppose Alice and Bob want to share a common secret through an insecure channel (by insecure, we mean Eve, an eavesdropper, can see every piece of information they share). The Diffie-Hellman shared secret exchange protocol allows them to do this.

The Diffie-Hellman protocol can be described using the following five-step process:

- **Step 1:** Either Alice or Bob selects a (large) prime number $p$ and a positive integer $g$ modulo $p.$ prime: $\: p$ positive integer: $\: g$ modulo $p.$ These public parameters are shared between the participants over the insecure channel, which means Eve can also see this information.

- **Step 2:** Next, Alice and Bob select their respective **private keys** $a$ and $b.$ The private keys are positive integers. They are not shared.

- **Step 3:** Alice and Bob now compute their respective **public keys,** $A$ and $B$ respectively, as follows: So, we now have the following key configuration:

- **Step 4:** Alice and Bob exchange their public keys $A$ and $B.$ Note that Eve can see both public keys.

- **Step 5:** Alice and Bob each compute the shared secret $s$ using the received public key and their private key as follows: So, finally, we have the following configuration.

Notice that Alice and Bob obtain the same value of $s.$ For Alice, we have

$$



s = B^a= (g^b)^a = g^{ab} \qquad (\text{mod }p),



$$

and for Bob, we have

$$



s = A^b= (g^a)^b = g^{ab}\qquad (\text{mod }p).



$$

Eve knows the values of $g^a$ and $g^b$ modulo $p,$ but does not know $s = g^{ab}$ modulo $p.$ The challenge of computing $g^{ab}$ given only $g, p$ and $g^a, g^b,$ modulo $p$ is known as the **Diffie-Hellman problem,** and is considered extremely hard for large primes $p.$ Additionally, certain choices of $g$ make the problem even more difficult for Eve.

### A Worked Example

Suppose Alice and Bob use the Diffie-Hellman key exchange protocol to construct a shared secret number. They use the public generator $g = 6$ and the prime modulus $41$ for this particular protocol. Alice's chosen secret key is $24,$ and Bob's secret key is $37.$ Let's compute the common shared secret obtained using the Diffie-Hellman algorithm with the given parameters.

For a Diffie-Hellman key exchange protocol with public generator $g$ and prime modulus $p$ between persons $A$ and $B$ with secret keys $a$ and $b,$ respectively, we have the following:

- Person $A$'s public key is given by

- Person $B$'s public key is given by

- The common shared secret is given by

With the given information, we can find the shared secret in two ways.

**Method 1**

Computing Alice's public key, we have

$$



\begin{aligned}𝐴 & ≡𝑔^{𝑎} & \,(mod\,𝑝) & \\ & ≡6^{24} & \,(mod\,41) & \\ & ≡16 & \,(mod\,41) & .\end{aligned}



$$

Therefore, the common shared secret is

$$



\begin{aligned}𝑆 & ≡𝐴^{𝑏} & \,(mod\,𝑝) & \\ & ≡16^{37} & \,(mod\,41) & \\ & ≡10 & \,(mod\,41) & .\end{aligned}



$$

**Method 2**

Computing Bob's public key, we have

$$



\begin{aligned}𝐵 & ≡𝑔^{𝑏} & \,(mod\,𝑝) & \\ & ≡6^{37} & \,(mod\,41) & \\ & ≡15 & \,(mod\,41) & .\end{aligned}



$$

Therefore, the common shared secret is

$$



\begin{aligned}𝑆 & ≡𝐵^{𝑎} & \,(mod\,𝑝) & \\ & ≡15^{24} & \,(mod\,41) & \\ & ≡10 & \,(mod\,41) & .\end{aligned}



$$

### Example: Applying the Diffie-Hellman Algorithm

#### Question

Alfred and Bernice use the Diffie-Hellman key exchange protocol to construct a shared secret number. They use the public generator $5$ and the prime modulus $37$ for this particular protocol. Alfred's chosen secret key is $34,$ and he is told that Bernice's public key is $20.$ Compute the common shared secret obtained using the Diffie-Hellman algorithm with the given parameters.

#### Explanation

For a Diffie-Hellman key exchange protocol with public generator $g$ and prime modulus $p$ between persons $A$ and $B$ with secret keys $a$ and $b,$ respectively, we have the following:

- Person $A$'s public key is given by

- Person $B$'s public key is given by

- The common shared secret is given by

Therefore, Alfred's and Bernice's common shared secret is

$$



\begin{aligned}𝑆 & ≡𝐵^{𝑎} & \,(mod\,𝑝) & \\ & ≡20^{34} & \,(mod\,37) & \\ & ≡21 & \,(mod\,37) & .\end{aligned}



$$
