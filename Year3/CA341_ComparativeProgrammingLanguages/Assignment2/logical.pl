%defines binary search tree node (left child less than item, right child greater than item)
bst(X, Left, Right):-
    Left < X, X < Right.

%recursively checks if item in binary tree
search(Item, bst(Item, _, _)).      %base case: if item is the same as current node
search(X, bst(Item, Left, _)) :-    %else if item to search is less than current item, traverse left
    X < Item, search(X, Left).
search(X, bst(_, _, Right)) :-      %else if item to search is greater than current item, traverse right
    search(X, Right).

%testing searching of tree (copy-paste to terminal)
%search(14, bst(10, bst(8, bst(2, nil, nil), bst(9, nil, nil)),bst(14,bst(11, nil, nil),bst(16, nil, nil)))).
%same thing as above, just for visual purposes:
search(100, bst(10, bst(8, bst(2, nil, nil), 
                           bst(9, nil, nil)
                        ),
                    bst(14, bst(11, nil, nil),
                            bst(16, nil, nil)
                        )
                )
        ).

%recursively checks for best position to add item to tree
%(i.e. adds an integer x into a binary tree T to give a binary tree R.)
insert(X, nil, bst(X, nil, nil)).                               %base case: if tree empty, item added as node
insert(X, bst(Item, Left, Right), bst(Item, Left2, Right)) :-   %else if item to add is less than current item, traverse left
    X < Item, insert(X, Left, Left2).
insert(X, bst(Item, Left, Right), bst(Item, Left, Right2)) :-   %else item to add is greater than current item, traverse right
    insert(X, Right, Right2).

%Inorder in the form (Left, Node, Right): 1 2 3 4 5
%traversing the tree then lists the nodes of the tree via inorder
inorder(nil, []).                               %base case: if tree is empty, creates empty list
inorder(bst(X, L, R), InorderLst) :-            %else recursively traverse left and right subtrees
    inorder(L, InorderL),
    inorder(R, InorderR), 
    append(InorderL, [X|InorderR], InorderLst). %keeps current node as head, and appending right lists to left lists

%Preorder in the form (Node, Left, Right): 2 1 4 3 5
%traversing the tree then lists the nodes of the tree via preorder
preorder(nil, []).
preorder(bst(X, L, R), PreorderLst) :-              %base case: if tree is empty, creates empty list
    preorder(L, PreorderL),                         %else recursively traverse left and right subtrees
    preorder(R, PreorderR), 
    append([X|PreorderL], PreorderR, PreorderLst).  %appending right lists to left lists

%Postorder in the form (Left, Right, Node): 1 3 5 4 2
%traversing the tree then lists the nodes of the tree via postorder
postorder(nil, []).                                 %base case: if tree is empty, creates empty list
postorder(bst(X, L, R), PostorderLst) :-            %else recursively traverse left and right subtrees
    postorder(L, PostorderL),
    postorder(R, PostorderR), 
    append(PostorderL, PostorderR, Postorder1),     %first add right lists to left lists
    append(Postorder1, [X], PostorderLst).          %then appending the current node to the Postorder1 list
