n=4;
p=5;
p1=1/8;
p2=1/8;
p3=1/8;
p4=1/8;
p5=1/8;
Pr=[p1;p2;p3;p4;p5];
M=20*n;
T=zeros(p,1);
S=zeros(p,M);
omega=[1/8;1/8;1/8;1/8;1/8]*3;
theta=omega./Pr;
C=n*omega;
N=1000;
T1=0;
T2=0;
T3=0;
T4=0;
T5=0;
T6=0;
T7=0;
T8=0;
T9=0;
T10=0;
h1=1.610308; 
h2=2.342534;
h3=2.999908;
h4=3.655500;
h5=4.351460;
h6=5.131867;
h7=6.064430;
h8=7.289276;
h9=9.236357;
for k=1:N
Y = grand(M, "mul", 1, Pr);
k1=0;
for j=1:M
    S(1,j)=sum(Y(1:1,1:j));
    if S(1,j)<= C(1) then k1=k1+1;
        end
end
k2=0;
for j=1:M
    S(2,j)=sum(Y(2:2,1:j));
    if S(2,j)<= C(2) then k2=k2+1;
        end
end
k3=0;
for j=1:M
    S(3,j)=sum(Y(3:3,1:j));
    if S(3,j)<= C(3) then k3=k3+1;
        end
end
k4=0;
for j=1:M
    S(4,j)=sum(Y(4:4,1:j));
    if S(4,j)<= C(4) then k4=k4+1;
        end
end
k5=0;
for j=1:M
    S(5,j)=sum(Y(5:5,1:j));
    if S(5,j)<= C(5) then k5=k5+1;
        end
end
T=[k1+1;k2+1;k3+1;k4+1;k5+1]/n;
PsiT=[(1/p1-1)*T(1),-min([T(1);T(2)]),-min([T(1);T(3)]),-min([T(1);T(4)]),-min([T(1);T(5)]);
-min([T(1);T(2)]),(1/p2-1)*T(2),-min([T(3);T(2)]),-min([T(4);T(2)]),-min([T(5);T(2)]);
-min([T(1);T(3)]),-min([T(2);T(3)]),(1/p3-1)*T(3),-min([T(4);T(3)]),-min([T(5);T(3)]);
-min([T(1);T(4)]),-min([T(2);T(4)]),-min([T(3);T(4)]),(1/p4-1)*T(4),-min([T(5);T(4)]);
-min([T(1);T(5)]),-min([T(2);T(5)]),-min([T(3);T(5)]),-min([T(4);T(5)]),(1/p5-1)*T(5)];
InvPsiT=inv(PsiT);
CT=(T-theta)'*InvPsiT*(T-theta);
ChiSquare=n*CT;

if ChiSquare<h1 then T1=T1+1;
    end
if h1<=ChiSquare & ChiSquare<=h2 then T2=T2+1;
    end
if h2<=ChiSquare & ChiSquare<=h3 then T3=T3+1;
    end
if h3<=ChiSquare & ChiSquare<=h4 then T4=T4+1;
    end
if h4<=ChiSquare & ChiSquare<=h5 then T5=T5+1;
    end
if h5<=ChiSquare & ChiSquare<=h6 then T6=T6+1;
    end
if h6<=ChiSquare & ChiSquare<=h7 then T7=T7+1;    
    end
if h7<=ChiSquare & ChiSquare<=h8 then T8=T8+1;
    end 
if h8<=ChiSquare & ChiSquare<=h9 then T9=T9+1;
    end
if h9<=ChiSquare then T10=T10+1;
    end
end
D=[T1,T2,T3,T4,T5,T6,T7,T8,T9,T10];
Percentage=(100/N)*D;
U=(Percentage-10).^2/10;
theta
T
Percentage
D
sum(U)








