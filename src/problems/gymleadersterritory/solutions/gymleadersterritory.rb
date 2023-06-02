n,k,m=gets.split.map(&:to_i)
g=Hash.new{|h,k|h[k]=[]}
m.times{a,b=gets.split.map(&:to_i);g[a]<<b;g[b]<<a}
visited=[false]*(n+1)
s=[[k,0]]
while !s.empty?
q,p=s.pop
visited[q]=true
g[q].each{|nbr|visited[nbr]?nbr!=p&&nbr==k&&(puts'NO';exit):s<<[nbr,q]}
end
puts'YES'
