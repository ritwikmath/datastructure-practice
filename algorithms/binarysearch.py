from typing import List

# 

contacts = [
    {"name": "Ivy Rodriguez", "phone": "901-234-5678", "email": "ivy.rodriguez@gmail.com"},
    {"name": "Alice Smith", "phone": "123-456-7890", "email": "alice.smith@gmail.com"},
    {"name": "Bob Johnson", "phone": "234-567-8901", "email": "bob.johnson@yahoo.com"},
    {"name": "Eve Jones", "phone": "567-890-1234", "email": "eve.jones@gmail.com"},
    {"name": "Charlie Williams", "phone": "345-678-9012", "email": "charlie.williams@outlook.com"},
    {"name": "David Brown", "phone": "456-789-0123", "email": "david.brown@example.com"},
    {"name": "Hank Davis", "phone": "890-123-4567", "email": "hank.davis@example.com"},
    {"name": "Frank Garcia", "phone": "678-901-2345", "email": "frank.garcia@yahoo.com"},
    {"name": "Jack Martinez", "phone": "012-345-6789", "email": "jack.martinez@yahoo.com"},
    {"name": "Grace Miller", "phone": "789-012-3456", "email": "grace.miller@outlook.com"},
]

target = "Frank Garcia"

class Solution:
    def search(self, contacts: List[dict], target: int):
        contacts.sort(key=lambda contact: contact["name"]) # To sort the contact
        # contacts = list(filter(lambda x: x["name"][0] == "A", contacts)) # To filter the result
        low = 0
        high = len(contacts) - 1
        while low <= high:
            mid = (low + high) // 2
            current = contacts[mid]["name"]
            if current == target:
                return contacts[mid]["phone"]
            if current < target:
                low = mid + 1
            else:
                high = mid - 1
        return None 
    
print(Solution().search(contacts.copy(), target))
