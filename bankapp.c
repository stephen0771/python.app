#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to hold bank account data
struct BankAccount {
    int accNo;
    char name[50];
    float balance;
};

// main functions 
void createAccount();
void depositMoney();
void withdrawMoney();
void checkBalance();
int main() {
    int choice;

    while (1) { // Loop to keep the program running until explicitly exited
        printf("\n--- Simple Banking System ---\n");
        printf("1. Create Account\n");
        printf("2. Deposit Money\n");
        printf("3. Withdraw Money\n");
        printf("4. Check Balance\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) { // Handling user input
            case 1: createAccount(); break;
            case 2: depositMoney(); break;
            case 3: withdrawMoney(); break;
            case 4: checkBalance(); break;
            case 5: exit(0);
            default: printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}

void createAccount() {
    FILE *file = fopen("bank_data.txt", "a");
    struct BankAccount acc;

    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }

    printf("Enter Account Number: ");
    scanf("%d", &acc.accNo);
    printf("Enter Account Holder Name: ");
    scanf("%s", acc.name);
    acc.balance = 0;

    fprintf(file, "%d %s %.2f\n", acc.accNo, acc.name, acc.balance); // Save to file
    fclose(file);
    printf("Account created successfully!\n");
}

void depositMoney() {
    int accNo, found = 0;
    float amount;
    FILE *file = fopen("bank_data.txt", "r");
    FILE *tempFile = fopen("temp.txt", "w");
    struct BankAccount acc;

    printf("Enter Account Number to deposit: ");
    scanf("%d", &accNo);
    printf("Enter Amount to Deposit: ");
    scanf("%f", &amount);

    while (fscanf(file, "%d %s %f", &acc.accNo, acc.name, &acc.balance) != EOF) {
        if (acc.accNo == accNo) {
            acc.balance += amount; // Update balance in memory
            found = 1;
        }
        fprintf(tempFile, "%d %s %.2f\n", acc.accNo, acc.name, acc.balance); // Rewrite all data
    }

    fclose(file);
    fclose(tempFile);
    remove("bank_data.txt");
    rename("temp.txt", "bank_data.txt");

    if (found) printf("Deposit Successful! New Balance: %.2f\n", acc.balance);
    else printf("Account not found!\n");
}

// withdraw money
void withdrawMoney() {
    int accNo, found = 0;
    float amount;
    FILE *file = fopen("bank_data.txt", "r");
    FILE *tempFile = fopen("temp.txt", "w");
    struct BankAccount acc;

    printf("Enter Account Number to withdraw: ");
    scanf("%d", &accNo);
    printf("Enter Amount to Withdraw: ");
    scanf("%f", &amount);

    while (fscanf(file, "%d %s %f", &acc.accNo, acc.name, &acc.balance) != EOF) {
        if (acc.accNo == accNo) {
            if (acc.balance >= amount) {
                acc.balance -= amount;
                found = 1;
            } else {
                printf("Insufficient balance!\n");
                fclose(file); fclose(tempFile); remove("temp.txt"); return;
            }
        }
        fprintf(tempFile, "%d %s %.2f\n", acc.accNo, acc.name, acc.balance);
    }

    fclose(file);
    fclose(tempFile);
    remove("bank_data.txt");
    rename("temp.txt", "bank_data.txt");

    if (found) printf("Withdrawal Successful! New Balance: %.2f\n", acc.balance);
    else printf("Account not found!\n");
}

void checkBalance() {
    int accNo, found = 0;
    FILE *file = fopen("bank_data.txt", "r");
    struct BankAccount acc;

    printf("Enter Account Number to check balance: ");
    scanf("%d", &accNo);

    while (fscanf(file, "%d %s %f", &acc.accNo, acc.name, &acc.balance) != EOF) {
        if (acc.accNo == accNo) {
            printf("Account Holder: %s\nBalance: %.2f\n", acc.name, acc.balance);
            found = 1;
            break;
        }
    }
    fclose(file);
    if (!found) printf("Account not found!\n");
}