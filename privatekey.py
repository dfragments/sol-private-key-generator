from solders.keypair import Keypair
import json
import base58  # Use the base58 library

output_file = "solana_wallets.txt"

wallets = []
with open(output_file, "w") as f:
    for i in range(500):
        keypair = Keypair()
        private_key = base58.b58encode(keypair.to_bytes()).decode()  # Convert private key to Base58

        wallet_data = {
            "index": i + 1,
            "private_key": private_key
        }
        wallets.append(wallet_data)
        
        f.write(json.dumps(wallet_data) + "\n")
        print(f"[{i+1}] Private Key: {private_key}")

print(f"\n✅ Successfully saved 500 private keys in {output_file}")
