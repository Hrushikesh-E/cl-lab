rows = input('Number of rows: ');
cols = input('Number of columns: ');
#in matlab input is considered as str
disp('Enter the elements of the first matrix (row-wise, separated by space):');
a = [];
for i = 1:rows
  #row_str is the variable used to store the input string for each row of the matrix(from source)
    row_str = input('', 's');
    #strsplit is used to split the input string into substrings
    #str2double to change substrings into numericals
    row_values = str2double(strsplit(row_str));
    if length(row_values) ~= cols
        disp('error:entered no of cols doent not match the given cols');
        break;
    end
    a = [a; row_values];
end

disp('Enter the elements of the second matrix (row-wise, separated by space):');
b = [];
for i = 1:rows
    row_str = input('', 's');
    row_values = str2double(strsplit(row_str));
    if length(row_values) ~= cols
        disp('error:entered no of cols doent not match the given cols');
        break;
    end
    b = [b; row_values];
end

sum= a + b;

disp('Sum of the two matrices:');
disp(sum);

