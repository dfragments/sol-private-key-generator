from solders.keypair import Keypair
import base58  # Use the base58 library

# Ask the user for the number of wallets to generate
num_wallets = int(input("Enter the number of wallets to create: "))

output_file = "keys.txt"

with open(output_file, "w") as f:
    for i in range(num_wallets):
        keypair = Keypair()
        private_key = base58.b58encode(keypair.to_bytes()).decode()  # Convert private key to Base58

        f.write(private_key + "\n")  # Save only the private key
        print(f"[{i+1}] Private Key: {private_key}")

print(f"\n✅ Successfully saved {num_wallets} private keys in {output_file}")
