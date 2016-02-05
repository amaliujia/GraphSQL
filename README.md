# GraphSQL
Graph Mining on SQL


### Relations

* Directed graph schema.
``` sql
TABLE GRAPH (src_id INT, desc_id INT, weight REAL)
```
note: Undirected graph schema is exaclty the same as directed graph, but each edge has doubly direction.

* Matrix schema
``` sql
TABLE MATRIX (row_id INT, col_id INT, value REAL)
```
* Vector schema
``` sql
TABLE VECTOR (id INT, value REAL)
``` 

### Fundemental SQL
- L2 norm of vector
``` sql
SELECT sqrt(sum((value)^2)) AS L2Norm FROM [vector table];
```
- vector dot product
``` sql
SELECT sum([vector table 1].value * [vector table 2].value) AS Dotproduct
FROM [vector table 1] INNER JOIN [vector table 2]
ON [vector table 1].id = [vector table 2].id;
```
- Matrix Multiplication (A X B)
``` sql
SELECT A.row_id, B.col_id, sum(A.value * B.value)
FROM [Matrix 1] AS A INNER JOIN [Matrix 2] AS B
ON A.col_id = B.row_id
GROUP BY A.row_id, B.col_id;
```
- Graph table times vector
``` sql
SELECT A.src_id, sum(A.weight, B.value)
FROM [Matrix 1] AS A INNER JOIN [Vector 1] AS B
ON A.col_id = B.id
GROUP BY A.src_id
```
- retrieve undirected graph from directed graph
``` sql
INSERT INTO [un_graph](src_id, dest_id, weight)
  SELECT src_id, dest_id, weight FROM [d_graph]
  UNION ALL
  SELECT dest_id "src_id", src_id "dest_id", weight FROM [d_graph];
```
