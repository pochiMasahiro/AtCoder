module Lib
    ( someFunc
    ) where

import Control.Monad

someFunc :: IO ()
someFunc = do 
  s <- replicateM 12 getLine
  putStrLn( show $ solve s)

solve :: [String] -> Int
solve s = length $ filter(\x -> elem 'r' x) s