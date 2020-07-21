% Catan board generator
%
% Board size, resource counts, number counts, and blank space locations can be
% modified by adjusting the values below. The following is assumed when these
% are updated:
%   resource_counts = rows * columns - blank_spaces
%   number_counts = resource_counts - desert_counts

% Constants that set the number of rows and columns
#const  rows    = 7.
#const  columns = 11.

% Set the number of resources, (Resource, Count)
resource(wheat,13).
resource(wood,12).
resource(ore,12).
resource(brick,12).
resource(sheep,12).
resource(desert,4). % a desert resource will be given a value of 0

% Set the number of numbers, (Number, Count)
number(2,5).
number(3,6).
number(4,7).
number(5,7).
number(6,6).
number(8,6).
number(9,7).
number(10,7).
number(11,6).
number(12,4).

% Place blank squares, each will be given a value of 0
blank(5,1).
blank(6,1).
blank(7,1).
blank(6,2).
blank(7,2).
blank(7,3).

blank(1,9).
blank(1,10).
blank(2,10).
blank(1,11).
blank(2,11).
blank(3,11).

% Choice generator for placing resources
{ place_resource(Row,Col,Res) : Row = 1..rows, Col = 1..columns, not blank(Row,Col) } = Cnt :- resource(Res,Cnt).
% Each space can only contain 1 resource
:- place_resource(Row,Col,Res1), place_resource(Row,Col,Res2), Res1 != Res2.

% Choice generator for placing numbers
{ place_number(Row,Col,Num) : Row = 1..rows, Col = 1..columns, not blank(Row,Col), not place_resource(Row,Col,desert) } = Cnt :- number(Num,Cnt).
% Each space can only contain 1 number
:- place_number(Row,Col,Num1), place_number(Row,Col,Num2), Num1 != Num2.
% No adjacent numbers can be identical
:- place_number(Row1,Col1,Num), place_number(Row2,Col2,Num), |Row1-Row2| + |Col1-Col2| = 1.
% No adjacent numbers can be 6 and 8
:- place_number(Row1,Col1,6), place_number(Row2,Col2,8), |Row1-Row2| + |Col1-Col2| = 1.

% build the board from the previous rules
board(Row,Col,desert,0) :- place_resource(Row,Col,desert).
board(Row,Col,blank,0) :- blank(Row,Col).
board(Row,Col,Res,Num) :- place_resource(Row,Col,Res), place_number(Row,Col,Num).


% we only display the board
#show board/4.

% Uncomment the following 2 lines to also get a count of all board spaces, this should match rows * cols if configured correctly
% board_size(Cnt) :- Cnt = #count { Row,Col : board(Row,Col,_,_) }.
% #show board_size/1.