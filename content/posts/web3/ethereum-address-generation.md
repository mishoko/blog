  

---
title: "Ethereum wallet generation process"
description: "A detailed guide on the Ethereum wallet generation process."
date: 2025-01-02
tags: ["ethereum", "address", "PBKDF2", "HMAC-SHA512", "hash", "seed", "wallet"]
draft: false
categories: ["web3", "security"]
mermaid: true

---

  

{{< mermaid >}}

  

graph TD;

a[mnemonic generation] -->|"+"| aa[passphrase]

aa -->|pbkdf2| b[bip39 seed generation]

b -->|hmac-sha512| c[bip32 root key]

c -->d[account level path: m/44'/60'/0']

d -->|ckdpriv| e[account extended private key]

e -->|secp256k1| f[account extended public key]

e -->|ckdpriv| h[bip32 extended private key]

h -->|secp256k1| i[bip32 extended public key]

h -->|derive child private key| g[address level path: m/44'/60'/0'/0]

g --> j[ethereum private key]

j -->|secp256k1| k[uncompressed public key]

k -->|remove 04 prefix| l[pure public key]

l -->|keccak-256| m[public key hash]

m -->|take last 20 bytes| n[address bytes]

n -->|eip-55 checksum| p[checksum address]

o -->|add 0x prefix| o[basic address]



  

%% example data flow

a1[/"spare warfare link hope moon soon ankle vanish ball judge roof rate"/] --> aa1

aa1["none / empty string (default)"] -->|pbkdf2| b1[/"seed: f5e6...a3b2 (512-bit)"/]

b1 -->|hmac-sha512| c1[/"master private key: 1837c1...cdf67\nmaster chain code: 3ddd56...b678"/]

c1 -->d1[/"m/44'/60'/0'"/]

d1 -->|ckdpriv| e1[/"xprvA1zY...PhViXSB3"/]

e1 -->|secp256k1| f1[/"xpub6CF...cfTk"/]

e1 -->|ckdpriv| h1[/"xprv9xpX...tuqncb"/]

h1 -->|secp256k1| i1[/"xpub6DFh...tYuQ"/]

h1 -->|derive| g1[/"m/44'/60'/0'/0"/]

g1 --> j1[/"private key: CE155FE8869...A9AA3044"/]

j1 -->|secp256k1| k1[/"public key: 0443ccc6509b0c1 ... 9d981f3e42d4"/]

k1 -->|remove 04| l1[/"43ccc6509...9d981f3e42d4"/]

l1 -->|keccak-256| m1[/"a297f6e2ad...73b4bf694e"/]

m1 -->|last 20 bytes| n1[/"57700b4f27e891b4bfb8da43d9ddb373b4bf694e"/]

n1 -->|eip-55| p1[/"57700B4f27E891B4bFB8dA43D9DDb373B4BF694E"/]

o1 -->|add 0x| o1[/"0x57700B4f27E891B4bFB8dA43D9DDb373B4BF694E"/]



  

%% styling

classDef process fill:#2d3748,stroke:#90cdf4,stroke-width:2px,color:#fff;

classDef example fill:#2a4365,stroke:#63b3ed,stroke-width:2px,color:#fff;

class a,aa,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p process;

class a1,aa1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1 example;

  

{{< /mermaid >}}
## Mnemonic generation

Example Mnemonic:

```text
spare warfare link hope moon soon ankle vanish ball judge roof rate
```
- 12 or 24 words from BIP39 word list. Could also be 3, 6, 9, 15, 18, 21 words (uncommon)
- Provides human-readable backup
- Entropy source for wallet generation
- Additional Details:
	- Entropy: The mnemonic is derived from entropy:
	- 128 bits of entropy → 12 words.
	- 256 bits of entropy → 24 words.
	- Checksum: A checksum is added to the entropy before converting it into words. For 128 bits of entropy, the checksum is 4 bits, making the total 132 bits. For 256 bits of entropy, the checksum is 8 bits, making the total 264 bits.

## Passphrase (optional)

  

  

  

Example Passphrase:

  

  

  

```text
"" -> none / empty string (default)
```

  

  

  

- Additional security layer

  

  

- Also called "13th word" or "25th word" respectively

  

  

- Combined with mnemonic before seed generation

  

  

  

- Additional Details:

  

- Use Case: The passphrase ensures that even if the mnemonic is compromised, the wallet cannot be accessed without the passphrase.

  

- Security: If the passphrase is lost, the wallet cannot be recovered.

  

  

  

## BIP39 seed generation

  

  

  

Input:

  

  

- Mnemonic + Passphrase

  

Process:

  

- run PBKDF2 function, 2048 iterations

  

  

Output:

  

- A 512-bit seed (64 bytes)

  

PBKDF2 parameters:

  

  

- Password = Mnemonic + Passphrase

  

  

- Salt = "mnemonic" + Passphrase

  

  

- Iterations = 2048

  

  

- Output length = 512 bits (64-byte)

  

  

  

Example:

  

  

- Input:

- Mnemonic: spare warfare link hope moon soon ankle vanish ball judge roof rate.

- Passphrase: "" (empty string).

- Output:

- Seed: 33c2b94ff6...fe30965ba (512 bits).


  

  

  

## BIP32 root key generation

  

  

Input:

  

- BIP39 Seed

  

Process:

  

- Use HMAC-SHA512 function with (key="Bitcoin seed", data=seed)

  

Note: The fixed string "Bitcoin seed" is always the same, regardless of the blockchain or wallet type

  

  

Output:

  

- BIP32 Root Key

  

  

Transformations details:

  

  

- From HMAC-SHA512 we get:

  

  

- Master Private Key: for ex: `1837C1...CDF67`

  

  

- Master Chain Code: for ex: `3DDD56...B678`

  

  

These components, along with metadata (version, depth, etc.), are combined into a binary structure.

  

  

- A checksum is added to the binary structure.

  

  

- The binary structure is Base58Check-encoded to produce the final xprv
for ex: `xprv9s21ZrQH143K44DCkvRhNBThD7gwnC7UfCjwyqqUMUq5ioVd4qGqAr1nxbYewmLTyWRRemQv8JBk6iNLRnaiJ7Y1ti9Wfbk4pztwQLwkvkk`
  

  

The **BIP32 Root Key** is the starting point for all key derivations in a hierarchical deterministic (HD) wallet.

  

  

  

## Derivation path specification

  

  

Standard Ethereum Path:

  

  

```text
m/44'/60'/0'/0/0
```

  

  

  

Path Breakdown:

  

  

- `m`: Master key (BIP32 Root Key).

  

  

- `44'` = BIP44 purpose

  

  

- `60'` = Ethereum coin type

  

  

- `0'` = Account index

  

  

- `0` = Change

  

  

- `0` = Address index

  

  

Additional Details:

  

- **Hardened derivation**, is indicated by the apostrophe (`'`). Hardened derivation uses the **private key** in the derivation process, making it more secure.

  

  

  

## Account extended private key (derived from BIP32 Root Key)

  

The Account Extended Private Key is derived from the BIP32 Root Key using the specified derivation path (e.g., m/44'/60'/0'/0).

- This is the account-level private key

- Used to derive all addresses for a single Ethereum account

- `Path: m/44'/60'/0'`

- `Format: xprv...`

  

Inputs:

- Parent Private Key: Derived from the previous step

- Parent Chain Code: Derived from the previous step.

- Index: 0' (hardened index = 0 + 2^31 = 2147483648).

Process:

1. CKDpriv Function:

- Concatenate:

- `0x00` (1 byte) + parent private key (32 bytes) + Index (4 bytes).

- Compute HMAC-SHA512:

-`Key: parent chain code.`

-`Data: Concatenated value above.`

- Split the 512-bit HMAC output into:

- Left 256 bits: New private key.

- Right 256 bits: New chain code.

2. Metadata:

- Depth: 4 (4 levels deep: m/44'/60'/0'/0).

- Parent Fingerprint: First 4 bytes of the hash of the parent public key.

- Child Index: `0'`

3. Serialization

- Combine the private key, chain code, and metadata.

- Add a checksum (4 bytes of the double SHA256 hash).

- Base58Check-encode the result.

  

Example:

- Parent Private Key: 0x4f8c1b...cdf67.

- Parent Chain Code: 0x6c7e8f...8f8f.

- Index: 0' (2147483648).

- Account Extended Private Key (xprv): `xprvA1zY..ViXSB3`

  
  

## Account extended public key (derived from account extended private key)

  

The account extended public key is derived from the Account Extended Private Key. It includes the public key, chain code, and metadata.

`Path: m/44'/60'/0'`

`Format: xpub...`

- Public counterpart of the Account Extended Private Key

- Can be used to generate public keys for multiple addresses without exposing private keys

  

Inputs:

- Account Extended Private Key (xprv): `xpub6CFfHpRTF...S7snBVy5escfTk`

  

Process:

1. Generate public key

- Compute the public key using secp256k1:

- `public key = private key * Generator Point (G).`

- Add the prefix 0x02 or 0x03 for compressed format.

1. Serialization:

- Combine the public key, chain code, and metadata.

- Add a checksum and Base58Check-encode the result.

  

Example:

- Account Public Key (Compressed): smt like. 0x02c1e7...df67.

- Account Extended Public Key (xpub):`xpub6CFfHpRTF9G52Qf...Vy5escfTk`

  

## BIP32 extended private key (derived from account extended private key)

  

The BIP32 Extended Private Key is derived from the account extended private key by updating the metadata to conform to the BIP32 standard.

`Path: m/44'/60'/0'/0`

`Format: xprv...`

- Used for generating individual ethereum private keys

- Each child key represents one ethereum address's private key

  

Inputs:

- Account Extended Private Key (xprv): `xprvA1zYh...PhViXSB3`

  

Process:

1. Update Metadata:

- Version: Change to BIP32 version (0x0488ADE4).

- Depth: increment by 1.

- Parent fingerprint: Calculate from the parent public key.

- Child index: Set to 0 (non-hardened).

1. Serialize:

- Combine the private key, chain code, and updated metadata into a binary structure.

- Add a checksum (4 bytes of the double SHA256 hash of the binary structure).

- Base58Check-encode the result to produce the BIP32 Extended Private Key (xprv).

  

Example:

- BIP32 extended private key (xprv): `xprvA1zYhyg4Cr...kUBPhViXSB3`

  

## BIP32 extended public key (derived from BIP32 extended private key)

  

The BIP32 Extended Public Key is derived from the BIP32 extended Private Key.

`Path: m/44'/60'/0'/0`

`Format: xpub...`

- Used for generating individual ethereum public keys

- Each child key represents one ethereum address's public key

  

Inputs:

- BIP32 extended Private Key (xprv): `xprvA1zYhyg4Cr...kUBPhViXSB3`

  

Process:

  

1. Generate Public Key: - Use the secp256k1 elliptic curve to compute the public key:

- Public Key = Private Key \* Generator Point (G)

2. Combine Metadata:

- Use the same metadata (depth, parent fingerprint, child index, chain code) from the BIP32 extended private key.

3. Serialize:

- Combine the public key, chain code, and metadata into a binary structure.

- Add a checksum (4 bytes of the double SHA256 hash of the binary structure).

- Base58Check-encode the result to produce the BIP32 Extended Public Key (xpub).

  

Example:

- BIP32 Extended Public Key (xpub): `xpub6Eyu7VCx3E...xczTVAfXq8EaW`

  

## Generate ethereum addresses

  

`For each index i:`

`Path: m/44'/60'/0'/0/i`

- Address: Keccak-256 hash of public key, take last 20 bytes

  
  

Example for first address (i=0):

1. BIP32 extended private Key (m/44'/60'/0'/0) `xprvA1zYhy...UBPhViXSB3`

2. Derive ethereum private key (m/44'/60'/0'/0/0) Private Key:  for ex: `CE155FE8869EBAF8...5BF1C3F4A9AA3044`

3. Generate public key: `43ccc6509b0c185..d981f3e42d4`

4. Remove the '04' Prefix

- The '04' prefix indicates an uncompressed public key- `e68acfc0253a...b7b6fba39`

5. Apply Keccak-256

- Take the Keccak-256 hash of the public key (without '04' prefix)

- hash: `5f27f5f6eb1f10c7d...18f85cd1d6d0f`

6. Extract the last 20 Bytes:

- Take the last 20 bytes (40 characters) of the Keccak-256 hash:

`9858EfFD232B4033E47d90003D41EC34EcaEda94`

7. Add '0x' prefix and apply capitalization rules (EIP-55 checksum)

- The mix of uppercase and lowercase letters is determined by the Keccak-256 hash.

- This mixed-case format allows wallets and tools to detect errors in the address

- Prepend '0x' to create the final Ethereum address

- `final address 0x9858EfFD232B4033E47d90003D41EC34EcaEda94`