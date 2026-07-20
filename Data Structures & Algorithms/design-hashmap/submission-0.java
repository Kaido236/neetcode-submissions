class MyHashMap {
    HashMap<Integer, Integer> hashmap = new HashMap<>();

    public MyHashMap() {

    }
    
    public void put(int key, int value) {
        this.hashmap.put(key,value);
    }
    
    public int get(int key) {
        if (this.hashmap.get(key) != null){
            return this.hashmap.get(key);
        }
        return -1;
    }
    
    public void remove(int key) {
        this.hashmap.remove(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */