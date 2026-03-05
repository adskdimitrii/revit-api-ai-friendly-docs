# Controlled Application Class

Source: https://www.revitapidocs.com/2026/35859972-2407-3910-cb07-bbb337e307e6.htm

---

| Controlled Application Class |
| --- |

Represents the Autodesk Revit Application with no access to documents. It provides options
and other application wide data and settings for external applications OnStartup/OnShutdown. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.ApplicationServices ControlledApplication 
  
**Namespace:** [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class ControlledApplication
```

```
Public Class ControlledApplication
```

```
public ref class ControlledApplication
```

```
type ControlledApplication = class end
```
The ControlledApplication type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ActiveAddInId](8e0bea86-9882-c8a5-4562-471989c6b56c.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AllUsersAddinsLocation](83a42cb4-37dc-d985-ed37-9326b7d06bbd.htm) | Add\-ins location for all users. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Cities](3a868628-038c-df32-df1b-2a6a55404c27.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Create](63042422-6c28-d8db-78f6-594c52701188.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CurrentUserAddinsLocation](df98bce4-9d9e-69fd-dc86-6071ca44ee92.htm) | Add\-ins location for current user. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CurrentUsersAddinsDataFolderPath](f83ab5b7-4ab5-6e2f-565e-c3bf0e46e44e.htm) | Path to AddinsData folder for the current user. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CurrentUsersDataFolderPath](3ff50826-aae6-0b19-8057-15af6a88cd41.htm) | Path to data folder for the current user. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsLateAddinLoading](d79bde46-2cd2-e13c-9c80-289e0d1968f4.htm) | Indicates whether this add\-in is loaded on the fly or not. If it is loaded when is Revit starting up, it is false, otherwise it should be true. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Language](1acafee6-95e0-50dd-2e46-8951e9405311.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Product](0c84ac5e-2054-a785-5551-e4eeb849b690.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RecordingJournalFilename](b51d0c47-7fd5-8c95-b99d-5456b5b97bc3.htm) | Retrieve the name of the journal file that Revit is currently recording to. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SharedComponentsLocation](Controlled-Application-Shared-Components-Location-Property.md) | Location of shared components used by Revit. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SharedParametersFilename](513e3512-4c82-4b20-b3e9-c33c3ee4cd61.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SubVersionNumber](9a13bb48-6d6f-002e-dd04-bfaaacdd51f6.htm) | The minor version number of Revit. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VersionBuild](c5963cab-c85b-561b-1ea2-b9d11b58050c.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VersionName](922cc2ba-ada9-9087-fc37-de8704e81218.htm) |  |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VersionNumber](35b18b73-4c47-fee3-d2f9-21298f029f7f.htm) |  |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetFailureDefinitionRegistry](c371a497-7110-9d90-0c04-c8024016fd4c.htm) | Returns the instance of FailureDefinitionRegistry. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLibraryPaths](c73eca5e-72d7-b75b-d47e-7ea2565b3920.htm) | Returns path information identifying where Revit searches for content. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsJournalPlaying](dcba9ff3-519f-0d86-b759-36be74d3c666.htm) | Determines if the application is currently in journal playback mode. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [OpenSharedParameterFile](6a8840aa-323f-3d4f-71cd-21be8da5af05.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [RegisterFailuresProcessor](5efdc31a-53b9-2ce4-5b72-837ae399be59.htm) | Registers Revit application\-wide instance of Failures Processor. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLibraryPaths](afa72cb3-6203-0a5c-c3b1-bd7fd49406fd.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [WriteJournalComment](9b5534bb-57f9-ec1e-c67d-fe507df28742.htm) | Writes a comment to the Revit journal file |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Events 

|  | Name | Description |
| --- | --- | --- |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ApplicationInitialized](1d917597-712c-cec3-db2a-8301c62a8ee3.htm) | Subscribe to this event to get notified after the Revit application has been initialized. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentChanged](f7acc5b4-a1b4-12ca-802b-0ee78942589e.htm) | Subscribe to the FailuresProcessingEvent event to be notified when Revit document has changed. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentClosed](b089cc05-ba85-03c2-e256-9f18ca7affc9.htm) | Subscribe to the DocumentClosing event to be notified when Revit is just about to close a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentClosing](2f0a7a6f-ed8b-0518-c5f8-edb14b321296.htm) | Subscribe to the DocumentClosing event to be notified when Revit is just about to close a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentCreated](89f514bf-f067-308d-0518-f050450bde72.htm) | Subscribe to the DocumentCreated event to be notified immediately after Revit has finished creating a new document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentCreating](5814928c-7794-395a-fdcd-5c3bd13b73ed.htm) | Subscribe to the DocumentCreating event to be notified when Revit is just about to create a new document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentOpened](7e5bc7a1-0475-b2ec-0aec-c410015737fe.htm) | Subscribe to the DocumentOpened event to be notified immediately after Revit has finished opening a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentOpening](99a0bcc4-fede-b66b-198d-a53f46ecf149.htm) | Subscribe to the DocumentOpening event to be notified when Revit is just about to open a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentPrinted](2bef4cd3-5ef7-8bf9-1d90-f6e9f875ac28.htm) | Subscribe to the DocumentPrinted event to be notified immediately after Revit has finished printing a view or ViewSet of the document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentPrinting](4f2f328a-3f67-4679-0f78-a5ee36ae95db.htm) | Subscribe to the DocumentPrinting event to be notified when Revit is just about to print a view or ViewSet of the document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentReloadedLatest](9b16d42f-2b88-d162-b266-8afa5222c439.htm) | Subscribe to the DocumentReloadedLatestEventArgs event to be notified immediately after Revit has finished reloading a document with central model. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentReloadingLatest](07307104-752f-e7da-b124-793dc35cb5ec.htm) | Subscribe to the DocumentReloadingLatestEventArgs event to be notified when Revit is just about to reload latest changes from a central model. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentSaved](bb944bb2-2141-4116-339f-4d13b6f6a6a5.htm) | Subscribe to the DocumentSaved event to be notified immediately after Revit has finished saving a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentSavedAs](5a68e38b-2156-eab1-c08b-dbc9a815b618.htm) | Subscribe to the DocumentSavedAs event to be notified immediately after Revit has finished saving document with a new file name. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentSaving](4a70d25a-c609-0e18-dad4-f34c7c349092.htm) | Subscribe to the DocumentSaving event to be notified when Revit is just about to save a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentSavingAs](ebfb171a-041e-636a-0c9e-62c4706cb146.htm) | Subscribe to the DocumentSavingAs event to be notified when Revit is just about to save the document with a new file name. This event is raised when Revit is just about to save the document with a new file name.  Note that the first save of a newly created document will raise DocumentSavingAs rather than [DocumentSaving](af9cc434-2934-d407-8ecf-960fc95ac569.htm) event. Handlers of this event are permitted to make modifications to any document (including the active document),  except for documents that are currently in read\-only mode. This event is cancellable, except when it is raised during close of the application.  Check the 'Cancellable' property of event's argument to see whether it is cancellable or not.  When it is cancellable, call the 'Cancel()' method of event's argument to cancel it.  Your application is responsible for providing feedback to the user about the reason for the cancellation. The following API functions are not available for the current document during this event: * [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm) and similar overloads. * [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm) . * [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm) and similar overloads.  Exception [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) will be thrown if any of the above methods is called during this event. Another event [DocumentSavedAs](6d3e2981-dfe0-fd33-9bd0-57e04815c4fd.htm) will be raised immediately after the document has been saved with a new file name. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentSynchronizedWithCentral](5cb6e92e-80b0-24e3-943c-a246566e4318.htm) | Subscribe to the DocumentSynchronizedWithCentral event to be notified immediately after Revit has finished synchronizing a document with central model. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DocumentSynchronizingWithCentral](20644173-bd8c-3598-4ac1-4c874679f8e8.htm) | Subscribe to the DocumentSynchronizingWithCentral event to be notified when Revit is just about to synchronize a document with central model. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ElementTypeDuplicated](470b50f6-5f49-a585-4b00-13b4131fb0c2.htm) | Subscribe to the ElementTypeDuplicated event to be notified immediately after Revit has finished duplicating an element type. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ElementTypeDuplicating](d4e741ea-cacc-a592-f2c1-ab2e4aa633bd.htm) | Subscribe to the ElementTypeDuplicating event to be notified when Revit is just about to duplicate an element type. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FailuresProcessing](388605d5-1096-6017-6b3b-f818a36eeffc.htm) | Subscribe to the FailuresProcessing event to be notified when failures are being processed at the end of transaction. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FamilyLoadedIntoDocument](8c607130-85f3-b6e4-bfb9-a9e2404022c1.htm) | Subscribe to the FamilyLoadedInto event to be notified after Revit loaded a family into a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FamilyLoadingIntoDocument](f6b8877c-57ae-f0f3-4a65-e87b26ebbd28.htm) | Subscribe to the FamilyLoadingInto event to be notified when Revit is just about to load a family into a document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FileExported](b319fd4a-07af-ddac-41a2-f1478d4ff100.htm) | Subscribe to the FileExported event to be notified immediately after Revit has finished exporting files of formats supported by the API. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FileExporting](c1f11a68-7712-17bf-dde3-04a077a7e6cf.htm) | Subscribe to the FileExporting event to be notified when Revit is just about to export files of formats supported by the API. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FileImported](53d944f4-4e2a-3625-d4cb-0eb454ed87aa.htm) | Subscribe to the FileImported event to be notified immediately after Revit has finished importing a file of format supported by the API. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FileImporting](5cd9ac35-6b1f-1084-c1f2-55d7dbc3b3ff.htm) | Subscribe to the FileImporting event to be notified when Revit is just about to import a file of format supported by the API. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [LinkedResourceOpened](4173dab8-f4da-ea8d-98c5-d6685349f159.htm) | Subscribe to the LinkedResourceOpened event to be notified immediately after Revit has finished opening a linked resource. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [LinkedResourceOpening](7b027897-ea2a-a1ac-18b4-c2bd6717923d.htm) | Subscribe to the LinkedResourceOpening event to be notified when Revit is just about to open a linked resource. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ProgressChanged](ec8d2e0e-dc55-d87b-b80a-32a0acce8246.htm) | Subscribe to the ProgressChanged event to be notified when an operation in Revit has progress bar data available. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ViewPrinted](08ae1e5f-e69a-421e-e04a-73f88711967a.htm) | Subscribe to the ViewPrinted event to be notified immediately after Revit has finished printing a view of the document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ViewPrinting](af45ed82-9ed8-ba3c-56fc-4df00af0cf35.htm) | Subscribe to the ViewPrinting event to be notified when Revit is just about to print a view of the document. |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [WorksharedOperationProgressChanged](9163633b-1939-f5a2-313a-ebb66aa062d0.htm) | \# Subscribe to the WorksharedOperationProgressChanged to be notified when progress has changed during Collaboration for Revit's workshared operations: open model and synchronize with central. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)
