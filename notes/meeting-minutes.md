# (Week 3)
- Role allocation
- Rough scenario
- Assigned:
  - Use cases (Jonathan)
  - GUI prototypes (Bob)
  - DevOps project/workflow set up (Oliver)

# Tuesday 14 Feb (Week 4)
- JJs Lab comments:
  - See Chesman and daniels, UML components, Chapter 4
    - Hotel reservation example
      - components and interfaces
      - use cases/requirements
  - Find examples online, choose best
  - Performance with 1000's of users, chain of hotels
- Discussion of scenario
- Using Python, Flask as web framework, SQL

# Friday 16 Feb (Week 4)
- Set goal on the issues board for next meeting
- Refined scenario
  #### Scenario: Hotel booking system

    - Role based (Actors)
      - Customer, managers, clerks, etc
    - Book room (see use cases)
      - Check if available
      - Offer an alternative
      - Assign room numbers
      - Special requirements for a user
      - Transactions
    - Cancel booking
    - Modify booking
    - Self service/reception

    - Multiple hotels (chain)
    - Shared DB, separated as schemas
      - Possible to move one or more schemas to another server/DB
        - Store DB info in configuration for each hotel
    - Backend separate from frontend
      - (Python) API exposed to frontend component
      - REST API exposed for other clients e.g. POS
      - MVC
    - JSON config
      - DB endpoint
      - Hotel config
        - Defaults
          - Room layouts
          - etc
      - 'Builds' the hotel(s) from a template

# Tuesday 21 Feb (Week 5)
Assigned tasks for sections 7 and 8


# Thursday 23 Feb (Week 5)
Discussion on candidate classes


# Friday 3 Mar (Week 6)
- Finishing
  - Classes - Patrick


- TODO
  - Interaction diagrams - Bob
  - ER diagrams - Jonney


- Assigned tasks
  - Implementation 1:
    - Basic project set up - Oliver
    - Database/SQLAlchemy mapping - Jonney
      - Roles - permissions table (look at wordpress)
        - RoleId
        - RoleName
        - each permission
      - Classes
        - Users
        - Room
        - Booking
        - RoomPrice

    - Set up nose testing - Bob

    - Patrick
      - Log in/log out
      - Reserve
      - Cancel

    - Bob
      - Check in
      - Check out

# Tuesday 7 Mar (Week 7)
JJs comments:

  - Suggested Patterns:
    - Decorator
    - Factory NB
    - Observer NB
    - Singleton


  - Features:
    - Composite/Staged bookings (Double and triple for Monday to Tuesday, double from Wednesday to Friday) - IN A SINGLE BOOKING
    - Discounts of various types
    - Customer types
    - Choice of hotel
    - Availability table (entity or control class?)


  - 3 use cases next week

  - Fix consistency problems between high level architecture and class diagram

  - Use separate packages rather than just classes for models

  - Fix interaction diagram



# Tuesday 14 Mar (Week 8)
Rest vs web services in report to show added value

Oliver:
- Vaildation
- List of permissions/roles
- SQLite test database

- View rooms

Jonney:
- View my reservations
- View other reservations
- (Finish DB + ER)

Paddy:
- Make reservation
- Cancel reservation
- (Finish SLC)

Bob:
- Check in
- Check out
- (Finish Nose testing)
