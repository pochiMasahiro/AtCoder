module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = do
  s <- getLine
  let ans = [x | x <- ['a'..'z'], not ( x `elem` s)]
  if (ans == []) then putStrLn "None" else putChar $ head ans 
