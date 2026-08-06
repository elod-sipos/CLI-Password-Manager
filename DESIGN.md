access: enter passkey

prompt: [G]et, [C]reate, [Q]uit

Get:
- ask for entry name
- ask for master pw
- derive key, find entry, decrypt
- show password

Create:
- ask for entry name
- use own password/ create new password
- if generate: creates password with set rules
- derive key from master pw (argon2id + salt)
- encrypt with AES-GCM, random nonce
- store {name, nonce, ciphertext} in vault file

