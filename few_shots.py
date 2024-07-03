few_shots = [
    {'Question' : "How many white color levi's t shirt we have left",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color='White'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "304"},
    {'Question': "How many is the price of inventory of all small size tshirt",
     'SQLQuery':"SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size = 'S'",
     'SQLResult': "Result of the SQL query",
     'Answer': "17775"},
     {'Question' : "How many Levis T shirt I have left" ,
      'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
      'SQLResult': "Result of the SQL query",
      'Answer' : "911"},
]