---

title: "Embrace hexadecimal - this is the way"

description: "hexadecimal is favored over binary in programming for its compactness, readability, and direct mapping to binary"

date: 2025-05-04

tags: ["data representation", "binary", "number systems", "programming fundamentals"]

draft: false

categories: ["web3"]

mermaid: true

---

#### TLDR


- Hexadecimal is favored over binary in programming for its compactness, readability, and direct mapping to binary.

- Each hex digit represents four binary digits, making conversions simple and reducing human error.

- Web2 developers rarely deal with raw binary or hex due to high-level abstractions, but web3 security researchers and auditors must understand hex for effective low-level analysis.

- Hex values make it easier to interpret storage slots, memory, and data structures in smart contracts and protocols.

- Mastery of hex is crucial for protocol analysis, debugging, reverse engineering, and security research in web3 environments.

- Examples:

- `0x14` (hex) = `10100` (binary) = `20` (decimal)

- `0xff` (hex) = `11111111` (binary) = `255` (decimal)

- 256-bit storage slot: 256 binary digits vs. 64 hex digits

When we dig into the internals of smart contracts, protocol specs, or low-level data structures, we’ll quickly notice a pattern: hexadecimal notation is everywhere, while binary is almost invisible. This isn’t just a matter of tradition—it’s a practical choice that impacts readability, accuracy, and efficiency. Let’s dig into why hex is favored

  

---

#### The Basics: How Number Systems Work in Programming

  

Computers operate on binary—sequences of 0s and 1s. On and off. Current passes through or not. Every value, from a single character to a massive cryptographic hash, is ultimately represented in binary at the hardware level. But for humans, binary is unwieldy. That’s where hexadecimal (base 16) comes in.

  

**Decimal (Base 10):**

This is the system we use every day. Each digit represents a power of 10.

  

**Binary (Base 2):**

Each digit is a 0 or 1, representing powers of 2. For example, the decimal number 500 in binary is:

  

```

500 (decimal) = 111110100 (binary)

```

  

**Hexadecimal (Base 16):**

Uses digits 0-9 and letters a-f. Each digit represents a power of 16. The same number, 500, in hex is:

  

```

500 (decimal) = 1f4 (hexadecimal)

```

  

---

  

#### Why Hexadecimal Is Preferred Over Binary

  

**1. Compactness and Readability**

Binary strings get long fast. A single byte in binary is eight digits:

  

```

Binary: 10101010

Hex: aa

```

  

A 256-bit value (common in Ethereum storage) is 256 binary digits, but only 64 hex digits. This makes hex much easier to scan, copy, and compare.

  

Fun fact: Even with LLM using hex over binary, reduces tokens and makes it easier to read.

  
  
  

**2. Direct Mapping to Binary**

Each hex digit corresponds exactly to four binary digits (a nibble). This makes conversion between the two systems straightforward and error-resistant.

  


|Hex|=> |Binary|

|0|  => |0000|

|1|  => |0001|

|2|  => |0010|

|...|=> |...|

|a|  => |1010|

|f|  => |1111|
  

**3. Byte Boundaries and Data Structure Clarity**

Two hex digits always represent one byte. (That's important when looking into the bytecode)

This makes it easy to see where bytes start and end, which is crucial when analyzing memory, storage, or serialized data.

  

**4. Human Error Reduction**

It’s easy to miscount or mistype a long string of 1s and 0s. Hex condenses this information, making mistakes less likely.

Also counting 0s in say a byte32 padded number is tedious for humans.

  

---

  

#### Practical Example: Ethereum Storage Slots

  

Let’s say we want to inspect a storage slot in a Solidity contract. Here’s what we might see:

  

**Raw 256-bit binary:**

  

```

00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010100

```

  

**Hexadecimal:**

  

```

0x0000000000000000000000000000000000000000000000000000000000000014

```

  

The hex version is not only shorter, but also much easier to interpret and communicate. You see , no scroll, lol.

  

---

  

#### Why Web2 Developers Rarely Worry About This

  

Most web2 developers work with high-level abstractions—strings, numbers, objects—where the underlying binary or hex representation is handled by the language or framework. Unless we’re dealing with low-level networking, file formats, buffers, or performance-critical code, one rarely needs to interpret raw binary or hex.

  

In contrast, web3 developers, security researchers, and auditors often need to analyze storage, calldata, or protocol messages at the byte or bit level. Here, understanding hex is essential.

  

---

  

#### Example: Converting Between Binary, Hex, and Decimal

  

Let’s look at a simple conversion:

  

- **Hex:** `0x14`

- **Binary:** `10100`

- **Decimal:** `20`

  

You can see how much more compact hex is compared to binary, and how easy it is to convert between them.

  

---

  

#### Example: Visualizing a Byte

  

Suppose you have a byte with the following binary value:

  

```

Binary: 11110000 // 2^0*0 + 2^1*0 + 2^2*0 + 2^3*0 + 2^4*1 + 2^5*1 + 2^6*1 + 2^7*1

```

  

In hex, this is simply:

  

```

Hex: f0 // caluclated as: 16^1*f + 16^0*0

// f is 15, so => 16*15 + 0

```

  

And in decimal:

  

```

Decimal: 240

```

  
  

This compactness is why hex is used for things like color codes (`#ff00ff`), MAC addresses, and memory dumps.

  

---

  

#### Why Security Researchers and Auditors Must Master Hex

  

- **protocol analysis:**

Many protocols (including Ethereum) specify data layouts in terms of bytes and nibbles. Hex makes it easy to see and manipulate these structures.

- **sending transactions, debugging and reverse engineering:**

When analyzing/preparing calldata, logs, or storage, hex is the standard. Tools like hexdump, block explorers, and debuggers all use hex.

- **bitwise operations:**

Understanding how hex maps to binary is crucial for bitwise logic, masking, and shifting—common tasks in security research.

- **error detection:**

Subtle bugs and vulnerabilities often hide in the details. Being able to quickly interpret hex can help you spot anomalies that would be invisible in binary or decimal.

  

---

  

#### Tips

  

- Remember: two hex digits = one byte. This helps when parsing or reconstructing data structures.

- forge/fondry has built-in converters

- when we see 0x this means we are looking at a hex value. 0x is there a hint.

- entire categories of bugs open up as we start to understand the hex and their dance in the evm

  

---

  
  

Understanding hex isn’t just a technical curiosity—it’s a practical skill that unlocks deeper insight into how data is stored, transmitted, and manipulated. For anyone working in web3 security or smart contract auditing, fluency in hex is a must-have. Learning more on the EVM, finding bugs in smart contracts or even applying concept like proxy contracts are dangerous when we have no idea of why hex is needed and/or represented.