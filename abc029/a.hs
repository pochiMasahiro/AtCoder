module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = getLine >>= \a -> putStrLn $ a ++ ['s']
