# Subelement Class

Source: https://www.revitapidocs.com/2026/2d15bb45-70af-5f84-e899-322742591251.htm

---

| Subelement Class |
| --- |

An object that represents an element or a subelement within the Autodesk Revit project. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB Subelement 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class Subelement : IDisposable
```

```
Public Class Subelement
	Implements IDisposable
```

```
public ref class Subelement : IDisposable
```

```
type Subelement = 
    class
        interface IDisposable
    end
```
The Subelement type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Category](0b0c9dba-f5ce-b20d-f883-5ef39bb4a6a5.htm) | Retrieves a Category object that represents the category or sub category of the subelement. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Document](5606267f-30e4-bd6c-8e06-43ad1f495585.htm) | The document in which the subelement resides. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Element](507946d2-87d1-ccc4-d174-7f5e789ceadd.htm) | The element in which the subelement resides. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](d1cfc136-56e5-614b-8d23-6b5ef2c7c874.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [TypeId](3480a4eb-8b80-c694-6a9b-9c5559cac920.htm) | The identifier of this subelement's type. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [UniqueId](2dd5798c-a4cd-edf1-b8c3-52f6cfc7e186.htm) | A stable unique identifier for this subelement within the document. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanHaveTypeAssigned](dec0c104-7808-4f07-9eb4-c9247cc3a65a.htm) | Identifies if the subelement can have a type assigned. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ChangeTypeId](4d8ab108-1a74-c4c9-1d84-ef323d246fe1.htm) | Changes the type of the subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Create](2df166ab-238b-1690-bd3e-2033778b9542.htm) | Creates an object representing element or subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](4e7a26fc-f9ec-e77b-cfdf-0f2c009bfb50.htm) | Releases all resources used by the Subelement |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAllParameters](f7ee81cc-3a1c-08c8-b495-c562968010cd.htm) | Returns all parameters of this subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetBoundingBox](32e76eb1-e305-ead5-0b3b-9eb15891c957.htm) | Retrieves a box that circumscribes all geometry of the subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetGeometryObject](be23471b-e6ba-472f-f960-06d7e3dce56a.htm) | Retrieve one geometric primitive representing given subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetParameterValue](c1af0433-3e94-6e40-429b-ad77aaeaff73.htm) | Obtains the current parameter value of this subelement given a parameter id. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetReference](62e0779b-25c1-b83a-0a13-ed2bf9cececc.htm) | Obtains the reference to this subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetValidTypes](e39919d5-4bca-bdf4-4e24-c73e03cf147a.htm) | Obtains a set of types that are valid for this subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [HasParameter](5725cdbe-5482-b403-f72f-936443e50e83.htm) | Checks if this subelement have given parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsParameterModifiable](82d6f753-6e14-3bd1-1fb2-caa284bf4686.htm) | Checks if given parameter of this subelement is modifiable. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsValidSubelementReference](89deea46-e7ab-6e7a-a363-665a2eb4b012.htm) | Checks if given Reference identifies either a valid element or subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValidType](b9ab1dbf-2b7b-398a-6682-e2cce94e4352.htm) | Checks if given type is valid for this subelement. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetParameterValue](b391bde2-d940-c022-8ab0-a86c7a083b64.htm) | Sets a new parameter value of this subelement given a parameter id. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Subelements provide a way for parts of an element to behave as though they were real elements without incurring the overhead of adding more full elements to the model. 

Many Revit features (for example parameters, schedules, and tags) were designed to operate on Elements.
 As a result, the Revit code needs to represent objects as Elements for them to participate in those features. This can lead to scalability problems,
 because every Element adds overhead and adding many Elements may decrease the performance of the model. An alternative is to use Subelements. An element
 can expose a set of "Subelements" that it contains, specifying characteristics like their category and parameters,
 and certain Revit capabilities will treat those Subelements the same as ordinary Elements. For example, a Subelement may contribute geometry to the main element
 and may be able to be selected independently of its parent Element. It will possibly have its own (settable) type as well as an assigned category which
 can be different from its parent Element. 

In the API, the new Subelement class is used to refer to either an Element or a specific subelement of a given Element.
 It is typically directly related to a Reference to either the Element or the specific subelement.
 Note that creation of new Subelements for a given element is not done generically. Instead, the given Element may provide the ability to modify it's definition,
 resulting in the creation of new Subelements. 

Examples of Elements which may have Subelements in practice include: 

* [RebarContainer](../Autodesk.Revit.DB.Structure/Rebar-Container-Class.md)
* [Rebar](../Autodesk.Revit.DB.Structure/Rebar-Class.md)
* [FabricSheet](../Autodesk.Revit.DB.Structure/Fabric-Sheet-Class.md)
* [Stairs](45e2c068-7e52-c84a-cfb8-a53c531d28fa.htm) elements which make up [MultistoryStairs](8b07cbff-013c-889f-8807-703e63a91923.htm) elements
* [Railing](4af1265f-859e-123b-ada5-a479324f3dee.htm)
* \[!:Autodesk::Revit::DB::Architecture::ContinuousRail]

To get access to a particular Subelement, you may use any of the following: 

* [Create(Document, Reference)](2df166ab-238b-1690-bd3e-2033778b9542.htm)
* [IsValidSubelementReference(Document, Reference)](89deea46-e7ab-6e7a-a363-665a2eb4b012.htm)
* Autodesk.Revit.DB.Document.GetSubelement(Autodesk.Revit.DB.Reference) if you have a Reference to a Subelement.
* Autodesk.Revit.DB.Document.GetSubelement(String) if you have a unique id of a Subelement.
* [GetSubelements](feabfd59-bd0f-ab61-34a1-d0d22f58c881.htm)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
