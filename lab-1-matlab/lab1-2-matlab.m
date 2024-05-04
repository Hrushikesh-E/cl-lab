a = [];
b = [];
d = input('Dimensions of vector: ');

for i = 1:d
    m = input(['element for a : ']);
    a = [a m];
end

for i = 1:d
    n = input(['element for b : ']);
    b = [b n];
end

disp('a =');
disp(a);
disp('b =');
disp(b);

prod = 0;
for i = 1:d
    prod = prod + a(i) * b(i);
end

disp('Dot product is ');
disp(prod);

