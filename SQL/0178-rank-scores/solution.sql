# Write your MySQL query statement below
WITH RANKING AS
(
    SELECT score,dense_rank()over(order by score desc) as "rank"
    from Scores
)
select * from ranking