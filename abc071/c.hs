module Lib
    ( someFunc
    ) where

import Data.List
someFunc :: IO ()
someFunc = do
  n <- getLine
  s <- getLine
  putStrLn $ show $ solve (filter (\x -> 2 <= length x) (group $ reverse $ sort $ map read $ words s)) (read n)

solve :: [[Int]] -> Int -> Int
solve ls n
  | n <= 4 && ls == [] || (length ls < 2) = 0
  | otherwise = if 4 <= length (head ls)  then (head (head ls)) * (head (head ls)) else (head $ head ls) * (head (ls!!1) )