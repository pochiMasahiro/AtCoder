module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = do 
  s <- getContents
  putStrLn . show . foldl1 lcm . map read . tail $ lines s
