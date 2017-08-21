module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = do
  s <- getLine
  putStrLn $ show $ solve $ map read $ words s

solve (a:b:c:d:_) = max 0 $ min b d - max a c