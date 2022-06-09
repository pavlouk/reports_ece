// refactored with guard clauses and return statements
void describeEating(Item item, Human eater) {
  if (item == null) {
    throw ArgumentError.notNull("item");
  }
  if (!item.isFood) {
    print("Wait, that's not even food!");
    return;
  }
  if (!eater.isFull && item.isDelicious) {
    print("Hmm, that was good.");
  } else if (eater.isFull) {
    print("I can't! Too full.");
  } else {
    print("Not bad. Nutritious.");
  }
  return;
}

void describeEating(Item item) {
  if (!item.isFood) {
    print("Wait, that's not even food!");
    return;
  }
  if (item.isDelicious) {
    print("Hmm, that was good.");
  } else {
    print("Not bad. Nutritious.");
  }
  return;
}

// before refactoring with guard clauses 
void describeEating(Item item, Human eater) {
  if (item != null) {
    if (!item.isFood) {
      print("Wait, that's not even food!");
    } else {
      if (!eater.isFull && item.isDelicious) {
        print("Hmm, that was good.");
      } else if (eater.isFull) {
        print("I can't! Too full.");
      } else {
        print("Not bad. Nutritious.");
      }
    }
  } else {
    throw ArgumentError.notNull("item");
  }
}

void describeEating(Item item) {
  if (!item.isFood) {
    print("Wait, that's not even food!");
  } else {
    if (item.isDelicious) {
      print("Hmm, that was good.");
    } else {
      print("Not bad. Nutritious.");
    }
  }
}