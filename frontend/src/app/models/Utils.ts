import omitDeep from 'omit-deep-lodash';

export class Utils {
  static removeUIDs = (object: Object) => {
    console.log(object);
    const clean = omitDeep(object, 'uid');
    console.log(clean);
    return clean;
  }
}
