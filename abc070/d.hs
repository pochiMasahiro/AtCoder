module Lib
    ( someFunc
    ) where

type node = Int
type cost = Int
data path = Path node node cost

someFunc :: IO ()
someFunc = putStrLn "someFunc"

find :: node -> tree -> (node, cost)
--find hp tree =

search :: node -> node -> [node] -> [path] -> cost -> cost
search hear dist route tree cost
  | hear == dist = cost
  | otherwise = map ((pnext, pcost) -> search pnext dist (route ++ pnext) tree (cost + pcost)) [(np, nc) <- find hear tree, np /= $ last route]