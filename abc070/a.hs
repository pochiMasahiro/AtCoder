module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = getLine >>= \a -> putStrLn (if(head a == last a) then "Yes" else "No")