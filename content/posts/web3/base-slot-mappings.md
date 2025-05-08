---   
title:  "Understanding the base slot in Solidity mappings?"

description: "base slot in mappings"

date: 2025-05-06

tags: ["storage", "storage layout"]

draft: false

categories: ["web3"]



---

#### What is the "base slot" in Solidity mappings?

Solidity’s mapping type is a cornerstone of smart contract development, powering everything from token balances to protocol state. But under the hood, the way mappings are stored is less obvious than with simple variables or arrays. Central to this storage model is the concept of the "base slot."

#### TLDR

- The “base slot” in Solidity is the storage slot assigned to a mapping variable, based on declaration order.
- Mapping values are not stored at the base slot; instead, the base slot is used with the key in a `keccak256` hash to compute each value’s unique storage slot.
- This design prevents collisions, enables constant-time access, and supports upgradeable contract patterns.
---
##### The basics: how Solidity assigns storage slots

Every state variable in a Solidity contract is assigned a storage slot—a numbered position in the contract’s private storage array. For simple variables, this is straightforward: the first variable gets slot 0, the next gets slot 1, and so on. Arrays and structs follow specific packing rules, but their storage is still sequential and predictable.

Mappings, however, are different. They can have an unbounded number of keys, and their values are not stored sequentially. Instead, Solidity uses a deterministic formula to calculate where each mapping value lives. And that's a good thing.

---

##### The base slot: the anchor for mapping storage

The "base slot" is the storage slot assigned to the mapping variable itself, based on its declaration order in the contract. For example:

```solidity

uint256 a; // slot 0  
mapping(address => uint256) balances; // slot 1 (base slot)  
```

Here, `balances` is assigned slot 1 as its base slot. But unlike simple variables, the base slot for a mapping does **not** directly store any values from the mapping. Instead, it acts as a unique anchor or "salt" for all key-value pairs in that mapping.

---

##### How mapping values are stored: the keccak256 formula

To find the storage slot for a specific mapping entry (e.g., `balances[0x123...]`), Solidity:

1. Pads the key (`address`) and the base slot to 32 bytes each.
2. Concatenates them: `abi.encodePacked(key, baseSlot)`.
3. Hashes the result with `keccak256`.
4. The resulting hash is the storage slot where the value for that key is stored.

So, the base slot is not where any mapping value is stored. Instead, it’s a critical part of the formula that ensures each key-value pair gets a unique, collision-resistant storage slot.

---

##### Why is the base slot important?

- **Prevents collisions:** The base slot ensures that different mappings (even with the same key type) never overlap in storage.
- **Enables deterministic access:** The combination of key and base slot guarantees that every mapping entry can be found in constant time, with no need for searching or iteration.
- **Supports upgradeability:** In upgradeable contracts, knowing the base slot of each mapping is essential for maintaining storage compatibility.

---

##### example

Suppose you have:


```solidity
mapping(address => uint256) public balances; // baseSlot = 2  
```


To store or retrieve `balances[0x8f997d1045639fedBddc856396A629d7257d4138]`, Solidity computes:

```
slot = keccak256(abi.encodePacked(  
    bytes32(uint256(0x8f997d1045639fedBddc856396A629d7257d4138)), // key padded to 32 bytes  
    bytes32(uint256(2)) // base slot  
))  
```

The value for that key is stored at `slot`, not at slot 2.

_Getting the keccak256 is actually very optimized in the EVM, so this is a very efficient way to access mapping values.
And no it is not prone to hash collisions._

---

##### Key takeaways for developers and auditors

- The base slot is the unique storage slot assigned to the mapping variable itself.
- It is not where mapping values are stored, but is used in the formula to compute each value’s actual storage slot.
- Understanding base slots is essential for low-level storage inspection, debugging, and contract upgradeability.

---

Understanding the base slot is fundamental for anyone working with Solidity at a low level, whether you’re building advanced protocols, auditing contracts, or debugging storage issues. It’s a small detail with a big impact on how data is organized and accessed in the EVM.