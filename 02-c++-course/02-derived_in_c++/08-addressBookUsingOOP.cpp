/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-27 04:28:19
 * @ As Known As: DarkStar0x714
 * @ Description: address book example to store and get data by user
 */

#include <bits/stdc++.h>

using namespace std;

class Person
{
public:
    string name;
    string address;
    string phoneNumber;

    Person(const string &n, const string &addr, const string &phone)
        : name(n), address(addr), phoneNumber(phone) {}
};

class AddressBook
{
private:
    vector<Person> users;

public:
    void listUsers()
    {
        for (auto &&user : users)
        {
            cout << "Name: " << user.name << "\tAddress: " << user.address << "\tPhone number: " << user.phoneNumber << endl;
        }
    }

    void addUser()
    {
        string name, address, phoneNumber;

        cout << "Enter user data: " << endl;

        cout << "Name: ";
        cin >> name;
        cout << endl;

        cout << "Address: ";
        cin.ignore(); // Clear the newline character left in the buffer
        getline(cin, address);

        cout << "phone number: ";
        cin >> phoneNumber;
        cout << endl;

        Person newPerson(name, address, phoneNumber);
        users.push_back(newPerson);

        cout << "User added successfully" << endl;
    }

    void deleteUser()
    {
        string name;
        cout << "Enter the name of the user to delete: ";
        cin >> name;

        auto it = find_if(users.begin(), users.end(), [name](const Person &user)
                          { return user.name == name; });

        if (it != users.end())
        {
            users.erase(it);
            cout << "User deleted successfully!" << endl;
        }
        else
        {
            cout << "User not found!" << endl;
        }
    }

    void deleteAllUsers()
    {
        users.clear();
        cout << "All users deleted successfully!" << endl;
    }

    void searchUser()
    {
        string name;
        cout << "enter user name to search: ";
        cin >> name;
        cout << endl;

        auto it = find_if(users.begin(), users.end(), [name](const Person &user)
                          { return user.name == name; });

        if (it != users.end())
        {
            cout << "user found in address book :" << endl;
            cout << "Name: " << it->name << "\tAddress: " << it->address << "\tPhone number: " << it->phoneNumber << endl;
        }
        else
        {
            cout << "User not found in address book";
        }
    }
};

enum Eoption
{
    List,
    Add,
    Delete,
    Delete_All,
    Search,
    Close,
    error
};

Eoption printOptions()
{
    cout << "Welcome to your favorite address book!" << endl;
    cout << "What do you want to do?, select a number or option name" << endl;
    cout << "| (1) List           | List all users" << endl;
    cout << "| (2) Add            | add an user" << endl;
    cout << "| (3) Delete         | delete an user" << endl;
    cout << "| (4) Delete All     | delete all users" << endl;
    cout << "| (5) Search         | Search for an user" << endl;
    cout << "| (6) Close          | Closes the address book" << endl;

    string option;
    cin >> option;

    Eoption userSelect;
    if (option == "1" || option == "List" || option == "list")
    {
        userSelect = Eoption::List;
    }
    else if (option == "2" || option == "Add" || option == "add")
    {
        userSelect = Eoption::Add;
    }
    else if (option == "3" || option == "Delete" || option == "delete")
    {
        userSelect = Eoption::Delete;
    }
    else if (option == "4" || option == "Delete All" || option == "delete all")
    {
        userSelect = Eoption::Delete_All;
    }
    else if (option == "5" || option == "Search" || option == "search")
    {
        userSelect = Eoption::Search;
    }
    else if (option == "6" || option == "Close" || option == "close")
    {
        userSelect = Eoption::Close;
    }
    else
    {
        userSelect = Eoption::error;
    }

    return userSelect;
}

int main()
{
    AddressBook addressBook;

    while (1)
    {
        Eoption userOption = printOptions();

        switch (userOption)
        {
        case Eoption::List:
            addressBook.listUsers();
            break;

        case Eoption::Add:
            addressBook.addUser();
            break;

        case Eoption::Delete:
            addressBook.deleteUser();
            break;

        case Eoption::Delete_All:
            addressBook.deleteAllUsers();
            break;

        case Eoption::Search:
            addressBook.searchUser();
            break;

        case Eoption::Close:
            cout << "Closing the address book. Goodbye!" << endl;
            return 0;

        case Eoption::error:
            cout << "Invalid option. Please try again." << endl;
        }
    }
}
