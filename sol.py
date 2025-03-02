import base58
from solders.keypair import Keypair
import json

output_file = "solana_wallets.txt"

wallets = []
with open(output_file, "w") as f:
    for i in range(500):
        keypair = Keypair()
        public_key = str(keypair.pubkey())  # Get public address
        private_key = base58.b58encode(keypair.to_bytes()).decode('utf-8')  # Convert private key to Base58

        wallet_data = {
            "index": i + 1,
            "public_key": public_key,
            "private_key": private_key
        }
        wallets.append(wallet_data)
        
        f.write(json.dumps(wallet_data) + "\n")
        print(f"[{i+1}] Public Key: {public_key} | Private Key: {private_key}")

print(f"\n✅ Successfully saved 500 wallets in {output_file}")
