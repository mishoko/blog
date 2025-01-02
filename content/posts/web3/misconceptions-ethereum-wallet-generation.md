---

title: "Common misconceptions (and clarifications) around the ethereum wallet generation process"

date: 2025-01-02

tags: ["ethereum", "wallets", "cryptocurrency"]

draft: false

categories: ["web3", "security"]

---


---

## Adding a passphrase to a mnemonic simply adds a small extra layer of security to the same wallet.

  

- Reality: Adding a passphrase to a mnemonic creates an entirely different set of wallets

The passphrase is combined with the mnemonic during the BIP39 seed generation process, resulting in a completely different seed.

For example:

Mnemonic: spare warfare link hope moon soon ankle vanish ball judge roof rate.

- With empty passphrase:

→ Seed: 33c2b94ff...7fe30965ba

→ Address m/44'/60'/0'/0/0: 0x2ec...Bbfd13a

- With passphrase "mySecretPassphrase":

→ Seed: df2bf439836...6d31e29e (completely different)

→ Address m/44'/60'/0'/0/0: 0xCb4578448a...448f8BbF (completely different)

  

- Gotcha: This means that even if someone has your mnemonic, they cannot access wallets created with a passphrase unless they also know the passphrase.

The passphrase feature allows users to create hidden wallets that are inaccessible without the passphrase, even if the mnemonic is compromised.

---

## One mnemonic = one wallet

- Misconception: Single mnemonic phrase corresponds to only one wallet.

- Reality: A single mnemonic phrase can generate an entire hierarchy of wallets.

This is the core idea behind hierarchical deterministic (HD) wallets. Using different derivation paths, you can generate multiple wallets (accounts) from the same mnemonic. For example:

  

m/44'/60'/0'/0/0 → First Ethereum address.

m/44'/60'/0'/0/1 → Second Ethereum address.

...

m/44'/60'/1'/0/0 → First Ethereum address in a different account.

  

This means that a single mnemonic can be used to manage multiple wallets across different blockchains (e.g., Bitcoin, Ethereum) and accounts.

  

---

  

## The mnemonic phrase is the same as the private key

  

- Misconception: Some confuse the mnemonic phrase with the private key.

  

- Reality: The mnemonic phrase is used to generate the BIP39 seed, which is then used to derive the private key. The mnemonic is not the private key itself.

  

---

## The BIP32 root key is blockchain-specific

  

- Misconception: The BIP32 root key or "Bitcoin Seed" string is blockchain-specific

- Reality: Both the BIP32 root key and the "Bitcoin seed" string are blockchain-agnostic. The "Bitcoin seed" string is a fixed constant in the BIP32 standard and is used in the HMAC-SHA512 function to generate the root key for all blockchains, including Ethereum. Similarly, the BIP32 root key itself is not tied to any specific blockchain. Instead, the derivation path (e.g., `m/44'/60'/0'/0/0`) determines the blockchain and account type. For Ethereum, the coin type is `60'`.

---

  

## The public key is directly used to generate ethereum addresses

  

- Misconception: The public key is directly used as the Ethereum address.

- Reality: The Ethereum address is derived from the Keccak-256 hash of the uncompressed public key. Specifically:

  

The uncompressed public key (64 bytes) is hashed using Keccak-256.

The last 20 bytes of the hash are used as the Ethereum address.

The address is prefixed with 0x.

  

---

  
  

## The depth field always matches the number of levels in the derivation path

  

- Misconception: The Depth field in the metadata always matches the number of levels in the derivation path. For example, for m/44'/60'/0'/0, they might think the depth is 5 because there are 5 components in the path.

  
  

- Reality: The Depth field starts at 0 for the BIP32 Root Key and increments by 1 for each level of derivation. For m/44'/60'/0'/0, the depth is 4 because:

  

m (Root Key) → Depth = 0.

44' → Depth = 1.

60' → Depth = 2.

0' → Depth = 3.

0 → Depth = 4.

  

---

  

## The mnemonic alone is sufficient to recover the wallet

  

Misconception: The mnemonic alone is sufficient to recover wallet

Reality: While the mnemonic is sufficient if no passphrase is used, if a passphrase was set during wallet creation, it is also required to recover the wallet. Without the passphrase, the wallet cannot be restored, even if the mnemonic is correct.

  

---

  

## Offline mnemonic generation guarantees 100% security

  

- Misconception: Offline mnemonic generation guarantees 100% security

- Reality: While generating a mnemonic offline significantly reduces the risk of online attacks, it does not eliminate all risks. Physical security of the device used for offline generation is critical. If the device is compromised (e.g., infected with malware before going offline) or if the mnemonic is improperly stored (e.g., written down and left in an insecure location), the wallet can still be compromised. Offline generation is just one part of a broader security strategy.

  

---

  

## Any English words can be used for a mnemonic

- Misconception: You can create a valid mnemonic using any English words you choose

- Reality: Valid mnemonics must use only words from the specific [BIP39 wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Each word in the list has been carefully chosen to minimize mistakes and ensure the first four letters of each word are unique. The wordlist is an essential part of the standard that ensures compatibility across all BIP39-compliant wallets. Using words outside this list will make it impossible to recover your wallet.

  

---

  

## Creating your own custom wordlist is fine

- Misconception: You can create your own wordlist as long as you remember it

- Reality: The BIP39 wordlist is not just a collection of random words - it's a precisely engineered list where words are chosen for specific properties: minimal similarity, error detection through word uniqueness, and efficient binary encoding. Each word represents a specific index that maps to binary data. Custom wordlists would break compatibility with all wallet software and could introduce vulnerabilities in the encoding process. Additionally, the checksum verification that ensures mnemonic integrity would fail with custom words.

  

---

## Any software or tool can be used to generate a mnemonic offline

- Misconception: A variety of tools can be used to generate a mnemonic offline

- Reality: Not all tools or software are trustworthy or compliant with the BIP39 standard. Using unverified or non-standard tools to generate a mnemonic offline can result in an invalid or insecure mnemonic. It’s crucial to use open-source, audited tools that adhere to the BIP39 standard to ensure compatibility and security. Additionally, the tool should be run in a secure offline environment, such as an air-gapped computer, to minimize risks.

---
