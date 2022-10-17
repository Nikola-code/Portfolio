const propertyIsEmpty = (property) => {
  return property.value === "" || property.value === undefined;
};

export default propertyIsEmpty;

