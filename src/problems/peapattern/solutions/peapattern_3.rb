n,m=gets.split;s=1
while n!=m&&s<101
n=(0..9).map{|j|k=n.count(j.to_s);k>0?"#{k}#{j}":""}.join
s+=1
end
puts n==m ? s: "Does not appear"