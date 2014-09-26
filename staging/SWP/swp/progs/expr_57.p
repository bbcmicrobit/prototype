defn setup:
    "places initial food and ants, returns seq of ant agents"
    [ ]
    sync nil:
        dotimes i food_places:
            let:
                p = place([rand_int (dim), rand_int (dim)])
            in:
                k = rand_int(food_range)
                alter:
                   p = assoc('food',k)
                endalter
            endlet
        enddotimes
        
        doall:
            for (x,y) in zip([home-range,home-range]):
                do:
                    alter:
                        place[x,y] = assoc('home',true)
                    endalter
                    create_ant((x,y), rand_int(8))
                enddo
            endfor
        enddo
    endsync
enddefn
