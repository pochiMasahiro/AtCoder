module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = do
  s <- getLine
  putStrLn $ solve $ map read $ words s

solve (x:a:b:_)
  |na < nb = "A"
  |na > nb = "B"
  where
    na = abs(x-a)
    nb = abs(x-b)