'''
4. Sample Tracker System for Lab
Idea: Tag each biological sample (DNA/protein) with a unique barcode or QR
📦 Features:

Auto-generate unique ID

Store sample info in dict or CSV

Print QR or barcode

Read back via scanner to load details

 Libraries: qrcode, uuid, csv, pyzbar
 DSA: Dict (sample info), UUID or auto-increment
'''
import uuid
import csv
import qrcode

def add_sample(sample_name, sample_type, storage_location):
    # Generate unique ID
    sample_id = str(uuid.uuid4())
    sample_info = {
        "SampleID": sample_id,
        "Name": sample_name,
        "Type": sample_type,
        "Location": storage_location
    }

    # Store in CSV
    with open("samples.csv", "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=sample_info.keys())
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow(sample_info)

    # Generate QR code
    qr = qrcode.make(sample_info)
    qr.save(f"{sample_id}.png")
    print(f"Sample added! ID: {sample_id}, QR code saved as {sample_id}.png")

# Example usage
if __name__ == "__main__":
    name = input("Enter sample name: ")
    typ = input("Enter sample type (DNA/protein/etc): ")
    loc = input("Enter storage location: ")
    add_sample(name, typ, loc)