#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// limiting the length/depth of infoNums and infoNames to 10
// (used for looping through it instead of hardcoding "10" everywhere)
int len = 10;

//struct for node
struct node {
    char *value;
    struct node *leftNode;
    struct node *rightNode;
};

// typedef makes calling the compare function easier
// typedef int (*Compare)(const char *, const char *);

//inserts elements into the tree
// assigns memory block for each element to be inserted
void insert(char* key, struct node** leaf){
    int result;
    // if current node is null, we add key there
    if(*leaf == NULL) {
        *leaf = (struct node*) malloc(sizeof(struct node));
        (*leaf)->value = malloc(strlen(key) + 1);     // setting memory for key
        strcpy((*leaf)->value, key);                   // copying the key (making it a node)
        (*leaf)->leftNode = NULL;
        (*leaf)->rightNode = NULL;
    }
    // else we compare the key to current node and add to correct position
    else{
        result = strcmp(key, (*leaf)->value);
        // if key is less than current node, insert to left subtree
        if(result < 0){
            insert(key, &(*leaf)->leftNode);
        }
        // if key is greater than current node, insert to right subtree
        else if(result > 0){
            insert(key, &(*leaf)->rightNode);
        }
        // else if key is equal to current node, already in tree, no insertion
        else{
            printf("Key '%s' already in tree\n", key);
        }
    }
}

//comparing value of new node against previous node
int compareStr(const char *a, const char *b){
    return (strcmp (a, b));     // comparing strings instead of pointers
}

//recursive function to print out the tree via inorder traversal
void in_order(struct node *root){
    // added the second condition to prevent printing '' chars that may've been added
    if(root != NULL && strlen(root->value) != 0) {
        in_order(root->leftNode);
        printf("    %s\n", root->value);
        in_order(root->rightNode);
    }
}

//searches elements in the tree recursively
// passes in key to insert, the tree to insert to, and cmp which is used for comparison
bool isPresent(char* val, struct node* leaf){
    int result;
    if(leaf != NULL){
        result = strcmp(val, leaf->value);
        // traverse left if val < current node
        if(result < 0)
            isPresent(val, leaf->leftNode);
        // traverse right if val > current node
        else if(result > 0)
            isPresent(val, leaf->rightNode);
        // else we found the node
        else{
            // printf("%s found!\n", val);
            return true;
        }
    }
    // else we didn't find it
    else{
        // printf("%s not in tree\n", val);
        return false;
    }
}

// finds minimum value of current node's subtree
struct node* FindMin(struct node* currNode){
    // minimum is in the left subtree so we keep going there
    while(currNode->leftNode != NULL){
        currNode = currNode->leftNode;
    }
    return currNode;
}

// recursively finds value to delete in tree
struct node* Delete(struct node *root, char val[]){
    if(root == NULL){
        return root;
    }
    // if val < root->value
    else if(strcmp(val, root->value) < 0){
        root->leftNode = Delete(root->leftNode, val);
    }
    // if(val > root->value)
    else if(strcmp(val, root->value) > 0){
        root->rightNode = Delete(root->rightNode, val);
    }
    // else we are on the node we want to delete
    else{
        // Case 1: no children present
        if((root->leftNode == NULL) && (root->rightNode == NULL)){
            free(root); //frees root from memory heap, make it null
            root = NULL;
        }
        // Case 2: one child present
        else if(root->leftNode == NULL){
            struct node *tempRoot = root;
            root = root->rightNode;     // new root is right child since left is null
            free(tempRoot);
        }
        else if(root->rightNode == NULL){
            struct node *tempRoot = root;
            root = root->leftNode;     // new root is left child since right is null
            free(tempRoot);
        }
        // Case 3: two children present
        // need to find the smallest value of right subtree to replace the current node
        else{
            struct node *tempRoot = FindMin(root->rightNode);
            root->value = tempRoot->value;
            root->rightNode = Delete(root->rightNode, tempRoot->value);
        }
    }
    return root;
}

// does same thing as python version
// passing in other tree, key, and value.
// e.g if contact is not in infoNames, it'll add it there, then check if it's in infoNums (or vice versa)
// this ensures that each entry has one copy and that copy is used in both trees.
void checkOtherTree(struct node* tree, char* key, char* value, char treeType[]){

    int check = isPresent(value, tree);
    if(check == 0){
        printf("%s (%s) was also not in %s. Adding...\n", value, key, treeType);
        insert(value, &tree);
    }
    else{
        printf("%s (%s) is already present in %s.\n", value, key, treeType);
    }
}

// does same thing as python version
// checks if contact in infoNames/infoNums, then checks if it's in infoNums/infoNames, respectively
void checkFirstTree(struct node* t1, struct node* t2, char lst[], char otherVal[]){

    // using this logic to check if it's a name (all phone numbers have same length, assuming names aren't as long as numbers)
    if(strlen(lst) != strlen(t1->value)){
        if(strlen(lst) != 0) {
            int check = isPresent(lst, t2);
            if(check == 0){
                printf("%s was not in infoNames. Adding...\n", lst);
                insert(lst, &t2);
            }
            checkOtherTree(t1, lst, otherVal, "infoNums");
        }
    }
    // else it's a name
    else{
        if(strlen(lst) != 0) {
            int check = isPresent(lst, t1);
            if(check == 0){
                printf("%s was not in infoNums. Adding...\n", lst);
                insert(lst, &t1);
            }
            checkOtherTree(t2, lst, otherVal, "infoNames");
        }
    }
    printf("\n");
    // return "Finished checking contacts\n";
}


int main(){

    // using the same data as OO approach for the binary trees

    // int len = 10;   // limiting the length of the list to 10
    // int width = 3;
    // int longestChar = 50;

    // mapping of contact number to name and address
    // Russell and Denise not in infoNames
    char infoNums[10][3][50] = {
            "0867898765", "Bob", "70 South Avenue",
            "0871122334", "Joe", "19 High Street",
            "0894234546", "Aaron", "90 Castle Road",
            "0899999999", "Denise", "120 Willow Lane",
            "1231231231", "Anakin", "4 Hillside House",
            "0897090909", "Russell", "59 St.Dixons Lane"
    };

    // mapping of name to contact number and address
    // Michael and Kenobi not in infoNums
    // length "dict", width, and num longest chars
    char infoNames[10][3][50] = {
            "Bob", "0867898765", "70 South Avenue",
            "Joe", "0871122334", "19 High Street",
            "Aaron", "0894234546", "90 Castle Road",
            "Michael", "0859071234", "Slough Avenue",
            "Kenobi", "0873454321", "12 George Road",
            "Anakin", "1231231231", "4 Hillside House"
    };

    char toBeAdded[10][3][50] = {
            "0873454321", "Kenobi", "12 George Road",
            "Denise", "0899999999", "120 Willow Lane",
            "DCU", "0851232321", "Glasnevin, Dublin 9",
            "Mick", "1800123212", "Ballymun",
            "0876789876", "Jonathan", "19 Meadow Park",
            "480268270", "UCD", "Dublin 4",
            "1231231231", "Anakin", "4 Hillside House",
            "Anakin", "1231231231", "4 Hillside House",
            "0859071234", "Michael", "Slough Avenue",
            "Michael", "0859071234", "Slough Avenue"
    };

    // tree1 stores phone numbers
    // tree2 stores names
    struct node *tree1 = NULL;  // initialising tree1 (infoNums) with NULL root
    struct node *tree2 = NULL;  // initialising tree2 (infoNames) with NULL root

    // initialising num/name to get current node for loop to add to tree1 or tree 2 respectively
    // "missing" used for adding missing contacts
    // "otherValue" gets the value which would be the key of other tree (i.e phone number in one tree is key in the other tree)
    char *name;
    char *num;
    char missing[50];
    char otherValue[50];

    // adding infoNums to tree 1
    for(int i = 0; i < len; i++){
        // we don't add empty items from infoNums
        if(strlen(*infoNums[i]) != 0){
            num = *infoNums[i];   // current num we're on in infoNums
            insert(num,  &tree1);
        }
    }
    // testing if a phone number has been added to tree1
    if(isPresent("0897090909", tree1) == 1){
        printf("%s found!\n", "0897090909");
    }
    else{
        printf("%s not in tree\n", "0897090909");
    }

    // adding infoNames to tree 2
    for(int i = 0; i < len; i++){
        // we don't add empty items from infoNames
        if(strlen(*infoNames[i]) != 0){
            name = *infoNames[i];   // current name we're on in infoNames
            insert(name, &tree2);
        }
    }
    // testing if a name has been added to tree2
    if(isPresent("Kenobi", tree2) == 1){
        printf("%s found!\n", "Kenobi");
    }
    else{
        printf("Key '%s' not in tree\n", "Kenobi");
    }

    printf("\nDeleting some contacts\n");

    // deleting one from tree 1, one from tree 2
    printf("Before:\n");
    in_order(tree1);    // outputs tree via inorder traversal
    printf("\n");
    in_order(tree2);
    isPresent("0871122334", tree1);    // checking if still in tree
    isPresent("Joe", tree2);    // checking if still in tree
    printf("Deleting 0871122334 and Joe from trees 1 and 2...\n");
    Delete(tree1, "0871122334");
    Delete(tree2, "Joe");
    isPresent("0871122334", tree1);    // should now be missing
    isPresent("Joe", tree2);    // should now be missing
    printf("After:\n");
    in_order(tree1);
    printf("\n");
    in_order(tree2);

    printf("\nAdding missing contacts\n");
    // adding "missing" contacts to trees
    for(int i = 0; i < len; i++){
        // we don't add empty items from toBeAdded (still need workaround for "Key '' already in tree" output)
        if(strlen(*toBeAdded[i]) != 0){
            strcpy(missing, *toBeAdded[i]);   // current missing we're on in toBeAdded
            strcpy(otherValue, toBeAdded[i][1]);
            // insert(missing, &tree2, (Compare)compareStr);
            checkFirstTree(tree1, tree2, missing, otherValue);
        }
    }

    return 0;
}
