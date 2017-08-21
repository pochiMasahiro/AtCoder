module Lib
    ( someFunc
    ) where

import Control.Monad
someFunc :: IO ()
someFunc = do
  n <- readLn :: IO Int
  let ans = replicateM n ['a'..'c']
  mapM_ putStrLn ans
