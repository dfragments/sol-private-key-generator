from solders.keypair import Keypair
import base58  # Use the base58 library

output_file = "solana_private_keys.txt"

with open(output_file, "w") as f:
    for i in range(500):
        keypair = Keypair()
        private_key = base58.b58encode(keypair.to_bytes()).decode()  # Convert private key to Base58

        f.write(private_key + "\n")  # Save only the private key
        print(f"[{i+1}] Private Key: {private_key}")

print(f"\n✅ Successfully saved 500 private keys in {output_file}")
