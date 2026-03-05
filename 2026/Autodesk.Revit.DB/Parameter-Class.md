# Parameter Class

Source: https://www.revitapidocs.com/2026/333ff41b-e6a7-d959-60bf-c3bfae495581.htm

---

| Parameter Class |
| --- |

The parameter object contains the value data assigned to that parameter. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) 
Autodesk.Revit.DB Parameter 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class Parameter : APIObject
```

```
Public Class Parameter
	Inherits APIObject
```

```
public ref class Parameter : public APIObject
```

```
type Parameter = 
    class
        inherit APIObject
    end
```
The Parameter type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Definition](dc30c65f-cfc4-244e-5a5c-bc333d7cd4c5.htm) | Returns the Definition object that describes the data type, name and other details of the parameter. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Description](Parameter-Description-Property.md) | Returns the tooltip information for a parameter. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Element](0645cb13-9c25-7f66-b22d-898832dc2ae3.htm) | The element to which this parameter belongs. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [GUID](50a62dcd-6027-9c69-377a-81fd96be88e8.htm) | The Guid for a shared parameter. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HasValue](2761a43b-3199-bbbb-6e6d-8ffd82febdec.htm) | Identifies if the parameter has an assigned value. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Id](8da1bd1e-581b-1577-6a58-579e11e25f2f.htm) | The id of the parameter. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsReadOnly](6b0e59ba-261f-65ab-901c-b9f2f033f651.htm) | Get the readonly property of the parameter. (Overrides [APIObject IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsShared](c1da6ced-7423-46a7-1c53-07c376987d17.htm) | Identifies if the parameter is a shared parameter. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [StorageType](9315853a-9210-6111-acba-8bd53913eec2.htm) | Describes the type that is used internally within the parameter to store its value. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [UserModifiable](99e14a83-f976-2465-6464-ed3f8a159000.htm) | Indicates whether the interactive user can modify the value of this parameter. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AsDouble](8831936d-965b-ec90-7e96-b2933c80b88e.htm) | Provides access to the double precision number within the parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AsElementId](3e05f5e6-72a2-f633-3740-93feecee8156.htm) | Provides access to the Autodesk::Revit::DB::ElementId^ stored within the parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AsInteger](507608fe-47fc-1441-acdc-5ce9c3c5da03.htm) | Provides access to the integer number within the parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AssociateWithGlobalParameter](796f3d95-956e-a2a9-7f8e-e8efd2a0eea0.htm) | Associates this parameter with a global parameter in the same document. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AsString](7aff8476-0396-fc08-27b4-467e4017f6a7.htm) | Provides access to the string contents of the parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AsValueString](5015755d-ee80-9d74-68d9-55effc60ed0c.htm) | Get the parameter value as a string with units. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AsValueString(FormatOptions)](b339e4f2-847b-c73a-91a6-034b134d30e7.htm) | Get the parameter value as a string with units. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeAssociatedWithGlobalParameter](f14bfd98-34de-ea9a-e34f-55631d23d466.htm) | Tests whether this parameter can be associated with the given global parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CanBeAssociatedWithGlobalParameters](fdbfc683-adc4-b722-c466-a605216a0ee4.htm) | Tests whether this parameter can be associated with any global parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ClearValue](14658620-d5d5-d8f2-1b6c-343180951d63.htm) | Clears the parameter to its initial value. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DissociateFromGlobalParameter](060e7402-6c92-06c2-d95b-1a79a3fad44a.htm) | Dissociates this parameter from a global parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAssociatedGlobalParameter](af5f333f-0d47-5f51-db38-bd6886905cf6.htm) | Returns a global parameter, if any, currently associated with this parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTypeId](03251b25-046d-1cd2-2b6d-85726f8593e5.htm) | Gets the identifier of the parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetUnitTypeId](fdcf8a82-e71b-ec72-4cd0-12e5de45517b.htm) | Gets the identifier of the unit quantifying the parameter value. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Set(Double)](a3e195e5-5601-2ffb-511b-693052137fa8.htm) | Sets the parameter to a new real number value. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Set(ElementId)](992097b4-0477-249f-581d-7903dfafd66d.htm) | Sets the parameter to a new element id. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Set(Int32\)](64a3ad4d-f2b9-632b-c99b-f09bd4d635ee.htm) | Sets the parameter to a new integer value. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Set(String)](956a1e23-cfe5-a60b-1ff9-0e8e33812774.htm) | Sets the parameter to a new string of text. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [SetMultiple](504f16ac-3842-d16f-3557-22fd787474c1.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetValueString](4218a8dc-1102-1766-8491-66e461e77ee5.htm) | Set the parameter value according to the input string. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The piece of data contained within the parameter can be either a Double, Integer,
String or ElementId. The parameter object can be retrieved from any Element object using
either a built in id, definition object or shared parameter guid. All Elements within
Autodesk Revit contain Parameters. These are options that can be accessed in a generic
fashion. Revit contains many built in parameter types but users and now developers, via the
API, can add their own parameters in the form of shared parameters. The developer should
become familiar with the Revit user interface for added and managing parameters and shared
parameters before using this API. The user interface components can be found in the following
locations: Element Properties dialog, Shared Parameters dialog (available from the File menu),
Project Parameters dialog (available from the Settings menu), Family Types dialog (available
from the Settings menu when editing a family). There are several relationships between the
objects that make up the APIs exposure of parameters. The parameter object contains the data
value. Parameter objects can be retrieved from Elements if you know its built\-in id,
its definition or its shared parameter guid. Each parameter has a definition. New parameters
can be added to Elements by adding a ParameterBinding object to the Document object. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
