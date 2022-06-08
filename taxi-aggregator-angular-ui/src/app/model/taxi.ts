export class Taxis {
  taxiList: Taxi[];
}

export class Taxi {
  _id: Id;
  name: string;
  type: string;
  timestamp: Date;
  location: Location;
}

export class Location {
  type: string;
  coordinates: number[];
}

export class Id {
  $oid: string;
}
