#include <iostream>
#include <string>
using namespace std;

// Node structure
struct Node {
    int prn;
    string name;
    Node* next;
};

// Linked List class
class Club {
private:
    Node* head;

public:
    Club() : head(nullptr) {}

    // Function prototypes
    Node* createNode(int prn, const string& name);
    void addPresident();
    void addSecretary();
    void addMember();
    void deletePresident();
    void deleteSecretary();
    void deleteMember(int position);
    void display();
    int countMembers();
    void reverseDisplay(Node* node);
    void reverse();
    void concatenate(Club& other);
    void menu();
};

// Create a new node
Node* Club::createNode(int prn, const string& name) {
    Node* newNode = new Node();
    newNode->prn = prn;
    newNode->name = name;
    newNode->next = nullptr;
    return newNode;
}

// Add president
void Club::addPresident() {
    int prn;
    string name;
    cout << "Enter President's PRN: ";
    cin >> prn;
    cout << "Enter President's Name: ";
    cin >> name;

    Node* newPresident = createNode(prn, name);
    newPresident->next = head;
    head = newPresident;
    cout << "New President Added!" << endl;
}

// Add secretary
void Club::addSecretary() {
    int prn;
    string name;
    cout << "Enter Secretary's PRN: ";
    cin >> prn;
    cout << "Enter Secretary's Name: ";
    cin >> name;

    if (!head) {
        cout << "No members present. Add a President first!" << endl;
        return;
    }

    Node* current = head;
    while (current->next) {
        current = current->next;
    }
    current->next = createNode(prn, name);
    cout << "New Secretary Added!" << endl;
}

// Add a member
void Club::addMember() {
    int prn;
    string name;
    cout << "Enter Member's PRN: ";
    cin >> prn;
    cout << "Enter Member's Name: ";
    cin >> name;

    Node* newMember = createNode(prn, name);
    if (!head) {
        cout << "No president found! Add a President first." << endl;
        return;
    }

    Node* current = head;
    while (current->next && current->next->next) {
        current = current->next;
    }
    newMember->next = current->next;
    current->next = newMember;
    cout << "New Member Added!" << endl;
}

// Delete president
void Club::deletePresident() {
    if (!head) {
        cout << "No President to delete!" << endl;
        return;
    }
    Node* toDelete = head;
    head = head->next;
    delete toDelete;
    cout << "President Deleted!" << endl;
}

// Delete secretary
void Club::deleteSecretary() {
    if (!head || !head->next) {
        cout << "No Secretary to delete!" << endl;
        return;
    }

    Node* current = head;
    while (current->next && current->next->next) {
        current = current->next;
    }
    Node* toDelete = current->next;
    current->next = nullptr;
    delete toDelete;
    cout << "Secretary Deleted!" << endl;
}

// Delete a member
void Club::deleteMember(int position) {
    if (position <= 0 || !head) {
        cout << "Invalid position!" << endl;
        return;
    }
    if (position == 1) {
        deletePresident();
        return;
    }

    Node* current = head;
    for (int i = 1; i < position - 1 && current->next; i++) {
        current = current->next;
    }
    if (current->next) {
        Node* toDelete = current->next;
        current->next = toDelete->next;
        delete toDelete;
        cout << "Member Deleted!" << endl;
    } else {
        cout << "No member at this position!" << endl;
    }
}

// Display members
void Club::display() {
    Node* current = head;
    if (!current) {
        cout << "No members in the club!" << endl;
        return;
    }
    cout << "Members: " << endl;
    while (current) {
        cout << "PRN: " << current->prn << ", Name: " << current->name << endl;
        current = current->next;
    }
}

// Count members
int Club::countMembers() {
    Node* current = head;
    int count = 0;
    while (current) {
        count++;
        current = current->next;
    }
    return count;
}

// Reverse display members
void Club::reverseDisplay(Node* node) {
    if (!node) return;
    reverseDisplay(node->next);
    cout << "PRN: " << node->prn << ", Name: " << node->name << endl;
}

// Reverse the list
void Club::reverse() {
    cout << "Reversed List:" << endl;
    reverseDisplay(head);
}

// Concatenate two lists
void Club::concatenate(Club& other) {
    if (!head) {
        head = other.head;
    } else {
        Node* current = head;
        while (current->next) {
            current = current->next;
        }
        current->next = other.head;
    }
}

// Menu for the club operations
void Club::menu() {
    while (true) {
        cout << "\nMenu: \n1. Add President \n2. Add Secretary \n3. Add Member \n4. Delete President \n5. Delete Secretary \n6. Delete Member \n7. Display Members \n8. Count Members \n9. Reverse Members \n10. Exit" << endl;
        int choice;
        cin >> choice;
        switch (choice) {
            case 1: addPresident(); break;
            case 2: addSecretary(); break;
            case 3: addMember(); break;
            case 4: deletePresident(); break;
            case 5: deleteSecretary(); break;
            case 6: {
                int pos;
                cout << "Enter position of member to delete: ";
                cin >> pos;
                deleteMember(pos);
                break;
            }
            case 7: display(); break;
            case 8: cout << "Total Members: " << countMembers() << endl; break;
            case 9: reverse(); break;
            case 10: return;
            default: cout << "Invalid choice! Try again." << endl; break;
        }
    }
}

// Main function
int main() {
    Club clubA, clubB;
    int choice;
    while (true) {
        cout << "Main Menu: \n1. Club A \n2. Club B \n3. Concatenate Clubs \n0. Exit" << endl;
        cin >> choice;
        switch (choice) {
            case 1: cout << "Club A Operations:" << endl; clubA.menu(); break;
            case 2: cout << "Club B Operations:" << endl; clubB.menu(); break;
            case 3: {
                Club combined;
                combined.concatenate(clubA);
                combined.concatenate(clubB);
                cout << "Combined Club Members:" << endl;
                combined.display();
                break;
            }
            case 0: return 0;
            default: cout << "Invalid choice! Try again." << endl; break;
        }
    }
}
