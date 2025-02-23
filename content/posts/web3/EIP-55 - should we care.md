
---
title: "EIP-55 - A highlevel dev perspective "
description: "A developer's guide on the EIP-55 process"
date: 2025-01-21
tags: ["ethereum", "address", "EIP-55", "wallet"]
draft: false
categories: ["web3", "security"]

---

This article dives into the **developer-focused benefits** of EIP-55, explains how it works, and provides a detailed example of converting an Ethereum address to EIP-55 format and validating its checksum.

---

## Why EIP-55 Matters

EIP-55 introduces a **mixed-case checksum** for Ethereum addresses, making it easier to detect errors caused by typos or incorrect capitalization. Without EIP-55, Ethereum addresses are **case-insensitive**, meaning users could enter an address in all lowercase or uppercase without issue. However, this also means that errors in the address cannot be easily detected, increasing the risk of sending funds to the wrong address.

By implementing (validate using) EIP-55, developers can:

- **Validate Ethereum addresses** with a checksum to prevent user errors.
- **Enhance security** by rejecting invalid or incorrectly formatted addresses.
- **Improve user/app/brand trust** by ensuring a smoother, error-free experience.
by just having the address the user is sending to. We just need to validating the address.

For wallets, displaying EIP-55 compliant addresses helps users avoid costly mistakes. For dApps, validating addresses before processing transactions ensures reliability and sticking to best practices.

---

## How EIP-55 Works: A dev perspective

EIP-55 works by applying a **checksum** to Ethereum addresses using the **Keccak-256 hash function**. The checksum determines the capitalization of each character in the address, making it possible to detect errors.

Here’s a step-by-step breakdown of how to convert an Ethereum address to EIP-55 format and validate its checksum.

---

### Example Data

Let’s use the following data to demonstrate the process:

| **Type**                         | **Value**                                                                                                                          |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Private Key                      | `DC1750CE96CE4D14CEE08C7300181F818172761BEC96B816EB322B190A8D1B6A`                                                                 |
| Public Key                       | `5acad9730f8232932558cbf68ae09f3dc7365e54172ca06086225be291ef316ceb68ce86414e4ec71f158542665b6fb7bf1b6bccf11606ef68c7600567eb0b22` |
| Ethereum Address (no checksum)   | `56a72e6cf4b2b2698708c5423db985d8251935fe`                                                                                         |
| Keccak-256 Hash of Address       | `2febcb3548b0838f919bfd107ec6d62dd995a2b42e209e02bfc4d67c325a40ac`                                                                 |
| Ethereum Address (with checksum) | `56A72E6cf4B2B2698708C5423DB985d8251935Fe`                                                                                         |

---

### Converting an address to EIP-55 Format

To convert an Ethereum address to EIP-55 format, follow these steps:

1. **Start with the Ethereum address in lowercase** (without the `0x` prefix):
    
    ```
    56a72e6cf4b2b2698708c5423db985d8251935fe  
    ```
    
2. **Hash the lowercase address using the Keccak-256 hashing algorithm**:
    
    ```
    keccak256('56a72e6cf4b2b2698708c5423db985d8251935fe') = 2febcb3548b0838f919bfd107ec6d62dd995a2b42e209e02bfc4d67c325a40ac  
    ```
    
3. **Determine capitalization based on the hash**:
    
    - For each character in the original address:
        - If the corresponding character in the hash (in binary) is **greater than or equal to 8**, the character in the address is **uppercase**.
        - Otherwise, the character is **lowercase**.
4. **Resulting EIP-55 Address**:
    
    ```
    56A72E6cf4B2B2698708C5423DB985d8251935Fe  
    ```

To better illustrate - let's put them next to each other:
```
56a72e6cf4b2b2698708c5423db985d8251935fe   // no checksum
2febcb3548b0838f919bfd107ec6d62dd995a2b4...// hash
56A72E6cf4B2B2698708C5423DB985d8251935Fe  // with chechsum i.e EIP-55
```
Here first 2 chars are numbers so we just copy them over, 3rd one is a, but it corresponds to e (hence is >=8) so we make it upper. Next one is 7 and 2 - numbers so we copy them over. Follows e, which is a b (>=8) so it ups. 6 is copies over. Next is c, which is a 5 (not >=8) so it keeps being small and so on.

---

### Validating an EIP-55 Address

To validate an Ethereum address with EIP-55 checksum, follow these steps:

1. **Remove the `0x` prefix** (if present):
    
    ```
    56A72E6cf4B2B2698708C5423DB985d8251935Fe  
    ```
    
2. **Convert the address to lowercase**:
    
    ```
    56a72e6cf4b2b2698708c5423db985d8251935fe  
    ```
    
3. **Hash the lowercase address using Keccak-256**:
    
    ```
    keccak256('56a72e6cf4b2b2698708c5423db985d8251935fe') = 2febcb3548b0838f919bfd107ec6d62dd995a2b42e209e02bfc4d67c325a40ac  
    ```
    
4. **Compare each character in the original address with the hash**:
    
    - For each character in the original address:
        - If the corresponding character in the hash (in binary) is **greater than or equal to 8**, the character in the address should be **uppercase**.
        - Otherwise, it should be **lowercase**.
5. **If the resulting address matches the original, the checksum is valid**.
    


---

## A Wallet is EIP-55 compliant If...

1. **It displays Ethereum addresses in the mixed-case checksum format**:
    - For example: `56A72E6cf4B2B2698708C5423DB985d8251935Fe`.
2. **It validates the checksum when you input an address**:
    - If the capitalization is incorrect, the wallet should reject the address as invalid. <== That's our implementation's main goal

---

## Why developers should implement EIP-55

1. **Prevent Costly Errors**: A single typo in an Ethereum address can result in permanent loss of funds. EIP-55 helps detect these errors before transactions are processed.
2. **Minimal Effort**: Most Ethereum libraries, already support EIP-55, making implementation straightforward. Also implementing the check 'from scratch' is trivial.
3. **Enhanced User Trust**: By validating addresses and displaying them in checksum format, you show users that your dApp or wallet prioritizes security and usability.