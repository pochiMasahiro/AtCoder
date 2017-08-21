module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = do 
  str <- getLine
  let n = read str :: Int
  putStrLn $ show $ calcf (n+1) (length str) 0 

calcf :: Int -> Int -> Int -> Int
calcf num order res
  | order == 0 = res
  | otherwise = calcf num (order-1) (res + ((num `div` (exp10 order)) * (exp10 $ order-1)) + calcs num (order-1) (num `mod` (exp10 order)))

calcs :: Int -> Int -> Int -> Int
calcs num order n2
  | n2 < (exp10 order) = 0
  | (exp10 order) <= n2 && n2 <= 2*(exp10 order) = n2 - (exp10 order)
  | (2*(exp10 order)) < n2 = exp10 order
  | otherwise = 0

exp10 :: Int -> Int
exp10 n
  | n == 0 = 1
  | otherwise = 10 * exp10 (n-1)
