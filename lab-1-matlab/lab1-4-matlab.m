rows = input('no of rows: ');
cols = input('no of columns: ');

if rows ~= cols
    disp('Error: Determinant can only be calculated for square matrices.');
else
    a = zeros(rows, cols);
    disp('Enter the elements of the matrix (row-wise, separated by space):');
    for i = 1:rows
        row_str = input('', 's');
        row_values = sscanf(row_str, '%f');
        if length(row_values) ~= cols
            disp('Error: Entered number of columns does not match the given columns');
            break;
        end
        a(i, :) = row_values;
    end

    det_result = det(a);
    disp(['Determinant of the matrix: ' num2str(det_result)]);
end

function result = det_2x2(matrix)
    result = matrix(1, 1) * matrix(2, 2) - matrix(1, 2) * matrix(2, 1);
end

function result = det(matrix)
    size_matrix = size(matrix);
    if size_matrix(1) == 1
        result = matrix(1, 1);
    elseif size_matrix(1) == 2
        result = det_2x2(matrix);
    else
        result = 0;
        for j = 1:size_matrix(2)
            x = matrix(2:end, [1:j-1, j+1:end]);
            result = result + ((-1)^(j+1)) * matrix(1, j) * det(x);
        end
    end
end

